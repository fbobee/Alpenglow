#ifndef MEMORY_RANKING_LOGGER_H
#define MEMORY_RANKING_LOGGER_H

#include "models/Model.h"
#include "utils/Ranking.h"
#include "loggers/Logger.h"
#include <vector>
#include <fstream>

struct RankingLog{
  double time;
  int id;
  int rank;
  int user;
  int item;
  double score;
  double prediction;
};

struct RankingLogs{
  int top_k;
  vector<RankingLog> logs;
};

struct MemoryRankingLoggerParameters{
  double min_time = 0;
  string out_file="";
  bool memory_log = true;
};

class MemoryRankingLogger
  : public Logger
//  , public NeedsExperimentEnvironment
//  , public Initializable
  {
  public:
    MemoryRankingLogger(MemoryRankingLoggerParameters* params){
      min_time_=params->min_time;
      if(params->out_file != ""){
        ofs.open(params->out_file.c_str());
      }
      memory_log_ = params->memory_log;
    }
    void set_model(Model* model){ model_ = model; }
    void set_rank_computer(RankComputer* rank_computer){ rank_computer_ = rank_computer; }
    void set_ranking_logs(RankingLogs* logs){ logs_=logs; }

    void run(RecDat* rec_dat){
      if(rec_dat->time >= min_time_ && rec_dat->eval==1){
        RankingLog log;
        log.time = rec_dat->time;
        log.rank = rank_computer_->get_rank(rec_dat);
        log.prediction = model_->prediction(rec_dat);
        log.item = rec_dat->item;
        log.user = rec_dat->user;
        log.score = rec_dat->score;
        log.id = rec_dat->id;
        if(memory_log_){
          logs_->logs.push_back(log);
        }

        if(ofs.is_open()){
          ofs 
            << (int) rec_dat->time << " "
            << log.rank << " "
            << log.prediction << " "
            << rec_dat->user << " "
            << rec_dat->item << " "
            << rec_dat->score << " "
            << rec_dat->id << endl;
        }
      }
    }
  private:
    ofstream ofs;
    RankingLogs* logs_ = NULL;
    double min_time_;
    Model* model_ = NULL;
    RankComputer* rank_computer_ = NULL;
    bool memory_log_;
};

#endif
