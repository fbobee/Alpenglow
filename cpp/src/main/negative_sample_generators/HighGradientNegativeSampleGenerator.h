#ifndef HIGH_GRADIENT_NEGATIVE_SAMPLE_GENERATOR_H
#define HIGH_GRADIENT_NEGATIVE_SAMPLE_GENERATOR_H

#include "NegativeSampleGenerator.h"
#include "../utils/SortPairDescendingBySecond.h"
struct HighGradientNegativeSampleGeneratorParameters {
  int negative_rate;
  int full_negative_rate;
  bool initialize_all;
  int max_item;
  int seed = 744478;
};
class HighGradientNegativeSampleGenerator : public NegativeSampleGenerator {
  public:
    HighGradientNegativeSampleGenerator(HighGradientNegativeSampleGeneratorParameters* params){
      negative_rate_=params->negative_rate;
      full_negative_rate_=params->full_negative_rate;
      random_.set(params->seed);
      model_=NULL;
      train_matrix_=NULL;
      initialize_all_ = params->initialize_all;
      if(initialize_all_){
        max_item_=params->max_item;
        generate_item_vector();
      } else {
        items_=NULL;
        max_item_=0;
      }
    }
    bool self_test(){
      bool ok=NegativeSampleGenerator::self_test() && random_.self_test();
      if(negative_rate_==-1){
        ok=false;
        cerr << "error: HighGradientNegativeSampleGenerator::negative_rate==-1" << endl;
      }
      if(full_negative_rate_==-1){
        ok=false;
        cerr << "error: HighGradientNegativeSampleGenerator::full_negative_rate==-1" << endl;
      }
      if(negative_rate_>full_negative_rate_){
        ok=false;
        cerr << "error: HighGradientNegativeSampleGenerator::negative_rate<full_negative_rate" << endl;
      }
      if(model_==NULL){
        ok=false;
        cerr << "error: HighGradientNegativeSampleGenerator::model is not set." << endl;
      }
      if(train_matrix_==NULL){
        ok=false;
        cerr << "error: HighGradientNegativeSampleGenerator::train_matrix is not set." << endl;
      }
      if(items_==NULL){
        ok=false;
        cerr << "error: HighGradientNegativeSampleGenerator::items_ is not set." << endl;
      }
      return ok;
    }
    void set_model(Model* model){
      model_=model;
    }
    void set_train_matrix(SpMatrix* train_matrix){
      train_matrix_=train_matrix;
    }
    void set_items(vector<int>* items){
      if(!initialize_all_) items_=items;
    }
    vector<int>* generate(RecDat* rec_dat);
  private:
    //config parameters
    int negative_rate_;
    int full_negative_rate_;
    int max_item_;
    bool initialize_all_;
    void generate_item_vector();
    Random random_;
    Model* model_;
    SpMatrix* train_matrix_;
    vector<int>* items_;
    //variables
    void generate_all();
    void choose_best();
    RecDat positive_sample_;
    int user_;
    int item_;
    vector<pair<int,double> > local_samples_;
};



#endif /* HIGH_GRADIENT_NEGATIVE_SAMPLE_GENERATOR_H */
