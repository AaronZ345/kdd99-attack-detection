from Mongo_Con import DB_manager
from All_Trainer import Trainer
from All_Predictor import Predictor


class All_Runner:
    trainer = Trainer()
    predictor = Predictor()

    def data_load(self):
        dataset, datatarget, T_len = self.db.All_fetch_data()
        return dataset, datatarget, T_len

    def train(self, dataset, datatarget, T_len):
        data_set, data_target, test_set, test_target = self.trainer.one_hot_encoding(dataset, datatarget, T_len)
        self.trainer.train(data_set, data_target)
        self.predictor.predict(test_set, test_target)

runner = All_Runner()
dataset, datatarget, T_len = DB_manager().All_fetch_data()
runner.train(dataset, datatarget, T_len)
print("all dowm")