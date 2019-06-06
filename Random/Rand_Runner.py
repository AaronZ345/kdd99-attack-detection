from Mongo_Con import DB_manager
from Rand_Trainer import Trainer
from Rand_Predictor import Predictor


class Rand_Runner:
    trainer = Trainer()
    predictor = Predictor()

    def data_load(self):
        dataset, datatarget, T_len = self.db.Rand_fetch_data()
        return dataset, datatarget, T_len

    def train(self, dataset, datatarget, T_len):
        data_set, data_target, test_set, test_target = self.trainer.one_hot_encoding(dataset, datatarget, T_len)
        self.trainer.train(data_set, data_target)
        self.predictor.predict(test_set, test_target)

runner = Rand_Runner()
dataset, datatarget, T_len = DB_manager().Rand_fetch_data()
runner.train(dataset, datatarget, T_len)
print("all dowm")