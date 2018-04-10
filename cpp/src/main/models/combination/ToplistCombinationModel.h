#ifndef TOPLIST_COMBINATION_MODEL
#define TOPLIST_COMBINATION_MODEL

#include <vector>
#include <set>
#include <gtest/gtest_prod.h>
#include "../Model.h"
#include "../RankingScoreIterator.h"
#include "../../general_interfaces/Initializable.h"
#include "../../general_interfaces/NeedsExperimentEnvironment.h"
#include "../../ranking/Ranking.h"
#include "../../utils/PredictionCreator.h"
#include "../../filters/DummyModelFilter.h"

using namespace std;

class ToplistCombinationModel
 : public Model,
   virtual public RankingScoreIteratorProvider,
   public Initializable,
   public NeedsExperimentEnvironment
{
public:
  void add_model(Model* model){
    models_.push_back(model);
  }
  void set_experiment_environment(ExperimentEnvironment* experiment_environment){ experiment_environment_ = experiment_environment; }
  bool self_test(){
    bool ok = Model::self_test();
    if(models_.size()==0) ok=false;
    for(auto rank_computer : rank_computers_) ok &= rank_computer->self_test();
    for(auto toplist_creator : toplist_creators_) ok &= toplist_creator->self_test(); 
    return ok;
  }
  void add(RecDat* rec_dat) override;
  double prediction(RecDat* rec_dat) override;
  void write(ostream& file) override;
  void read(istream& file) override;
  RankingScoreIterator* get_ranking_score_iterator(int user) override;
  ~ToplistCombinationModel(){
    for(auto rank_computer: rank_computers_){ delete rank_computer; }
    for(auto toplist_creator: toplist_creators_){ delete toplist_creator; }
    rank_computers_.clear();
  }
protected:
  bool autocalled_initialize(){
    random_=experiment_environment_->get_random();
    top_k_=experiment_environment_->get_top_k();
    distribution_.clear(); //should not be called twice, but...
    distribution_.resize(models_.size(),1.0/models_.size());
    dummy_model_filter_.set_experiment_environment(experiment_environment_);
    bool ok = true;
    ok &= dummy_model_filter_.initialize();
    for(auto model : models_){
      RankComputerParameters rank_computer_params;
      rank_computer_params.top_k=top_k_;
      rank_computer_params.random_seed=19263435; //TODO get rid of random seed here, RankComputer should use the common random object
      RankComputer* rank_computer = new RankComputer(&rank_computer_params);
      rank_computers_.push_back(rank_computer);
      rank_computer->set_experiment_environment(experiment_environment_);
      rank_computer->set_model(model);
      ok &= rank_computer->initialize();
      PredictionCreatorPersonalizedParameters toplist_computer_params;
      PredictionCreatorPersonalized* toplist_creator = new PredictionCreatorPersonalized(&toplist_computer_params);
      toplist_creators_.push_back(toplist_creator);
      toplist_creator->set_experiment_environment(experiment_environment_);
      toplist_creator->set_model(model);
      toplist_creator->set_filter(&dummy_model_filter_);
      ok &= toplist_creator->initialize();
    }
    return ok;
  }
private:
  void recompute_predictions(RecDat* rec_dat);
  bool random_values_generated_ = false;
  void generate_random_values_for_toplists();
  vector<int> random_model_indices_;
  void compute_score_map();
  map<int,double> scores_;
  void compute_last_occ_of_models();
  vector<int> last_occ_of_models_;
  bool test_top_k(RecDat*);
  void compute_toplists(RecDat* rec_dat);
  vector<vector<pair<int,double>>> toplists_; //models->toplist->(item,score)
  void merge_toplists();
  vector<pair<int,double>> toplist_;

  vector<Model*> models_;
  vector<RankComputer*> rank_computers_;
  vector<PredictionCreatorPersonalized*> toplist_creators_;
  DummyModelFilter dummy_model_filter_;
  vector<double> distribution_;
  //cache
  double last_timestamp_ = -1;
  int last_user_ = -1;
  int last_id_ = -1;
  Random* random_ = NULL;
  int top_k_ = -1;
  ExperimentEnvironment* experiment_environment_ = NULL;
  FRIEND_TEST(TestToplistCombinationModel, generate_random_values_for_toplists);
  FRIEND_TEST(TestToplistCombinationModel, compute_last_occ_of_models);
  FRIEND_TEST(TestToplistCombinationModel, test_top_k);
  FRIEND_TEST(TestToplistCombinationModel, compute_toplists);
  FRIEND_TEST(TestToplistCombinationModel, merge_toplists);
  FRIEND_TEST(TestToplistCombinationModel, prediction);
  //friend class RandomChoosingCombinedModelExpertUpdater;
};

#endif
