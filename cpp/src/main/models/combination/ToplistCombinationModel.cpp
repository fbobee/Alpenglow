#include "ToplistCombinationModel.h"

void ToplistCombinationModel::add(RecDat* rec_dat){
  for(auto model:models_){
    model->add(rec_dat);
  }
}
double ToplistCombinationModel::prediction(RecDat* rec_dat){
  if(rec_dat->id == last_id_ and rec_dat->user==last_user_ and rec_dat->time ==last_timestamp_){
    compute_score_map();
    return scores_[rec_dat->item]; //TODO return 0 if item is not in the map
  }
  if(!random_values_generated_){
    generate_random_values_for_toplists();
    compute_last_occ_of_models();
    random_values_generated_ = true;
  }
  if (!test_top_k(rec_dat)) return 0; //toplist should be cleared? Not exactly.
  compute_toplists(rec_dat);
  merge_toplists();
  last_id_ = rec_dat->id;
  last_user_ = rec_dat->user;
  last_timestamp_ = rec_dat->time;
  return 0; //TODO find index of the item, return 1/(index+1)
}
void ToplistCombinationModel::write(ostream& file){
  for(auto model:models_){
    model->write(file);
  }
}
void ToplistCombinationModel::read(istream& file){
  for(auto model:models_){
    model->read(file);
  }
}

RankingScoreIterator* ToplistCombinationModel::get_ranking_score_iterator(int user){
  if(user!=last_user_) throw exception(); //prediction should be called first, the parameter here is user, not recdat, we can't update state fields properly
  return NULL; //TODO
}

void ToplistCombinationModel::generate_random_values_for_toplists(){
  random_model_indices_.clear();
  for(int i=0;i<experiment_environment_->get_top_k();i++){
    random_model_indices_.push_back(random_->get_discrete(distribution_));
  }
}
void ToplistCombinationModel::compute_score_map(){}
void ToplistCombinationModel::compute_last_occ_of_models(){
  last_occ_of_models_.clear();
  last_occ_of_models_.resize(models_.size(),-1);
  for(uint i=0;i<random_model_indices_.size();i++){
    int model = random_model_indices_[i];
    last_occ_of_models_[model]=i;
  }
}
bool ToplistCombinationModel::test_top_k(RecDat* rec_dat){
  for(uint i=0;i<models_.size();i++){
    int rank = rank_computers_[i]->get_rank(rec_dat);
    if(rank<=last_occ_of_models_[i]) return true;
  }
  return false;
}
void ToplistCombinationModel::compute_toplists(RecDat* rec_dat){
  toplists_.clear();
  toplists_.resize(models_.size());
  for(uint i=0;i<toplists_.size();i++){
    toplists_[i].resize(last_occ_of_models_[i]+1);
  }
  for(uint i=0;i<toplist_creators_.size();i++){
    vector<RecDat>* toplist = toplist_creators_[i]->run(rec_dat);
    for(uint j=0;j<toplists_[i].size();j++){
      toplists_[i][j].first = toplist->at(j).item;
      toplists_[i][j].second = toplist->at(j).score;
    }
  }
}
void ToplistCombinationModel::merge_toplists(){}
