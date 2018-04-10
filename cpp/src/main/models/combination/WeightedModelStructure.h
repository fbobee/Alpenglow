#ifndef WEIGHTED_MODEL_STRUCTURE
#define WEIGHTED_MODEL_STRUCTURE

#include <vector>
#include "../Model.h"


struct WeightedModelStructure{
  vector<Model*> models_;
  vector<double> distribution_;
  bool is_initialized(){ return initialized_; }
private:
  bool initialized_ = false;
  friend class RandomChoosingCombinedModel;
  friend class ToplistCombinationModel;
};

class WMSUpdater{
public:
  virtual void set_wms(WeightedModelStructure* wms)=0;
};

#endif
