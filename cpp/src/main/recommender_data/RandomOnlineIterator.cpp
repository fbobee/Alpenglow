#include "RandomOnlineIterator.h"

RecDat* RandomOnlineIterator::get_actual(){
  return shuffled_data_[counter_-1];
}

RecDat* RandomOnlineIterator::get(int index) const {
  if(index>=counter_) throw exception();
  return shuffled_data_[index];
}

RecDat* RandomOnlineIterator::get_future(int index) const {
 return shuffled_data_[index];
}
RecDat* RandomOnlineIterator::next(){
  return shuffled_data_[counter_++];
};
void RandomOnlineIterator::restart(){
  if(shuffle_mode_ == "auto_shuffle") shuffle();
  counter_ = 0;
};
void RandomOnlineIterator::shuffle() {
  //random_shuffle(shuffled_data_.begin(),shuffled_data_.end(),random_);
};
double RandomOnlineIterator::get_following_timestamp() const {
  if(counter_ < recommender_data_->size()){
    RecDat* next = shuffled_data_[counter_];
    return next->time;
  } else {
    return -1;
  }
}

bool RandomOnlineIterator::autocalled_initialize() {
  if(!parent_is_initialized_){
    parent_is_initialized_=RecommenderDataIterator::autocalled_initialize();
    if(!parent_is_initialized_) return false;
  }
  shuffled_data_.resize(recommender_data_->size());
  for(int i=0;i<recommender_data_->size();i++){
    shuffled_data_[i]=recommender_data_->get(i);
  }
  restart();
  return true;
}
