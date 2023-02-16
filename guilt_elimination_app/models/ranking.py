
import collections
# defaultdictdict使ってyをカウントする
import csv
import os
import pathlib

RANKING_COLUMN_FOOD_NAME = 'FOOD NAME'
RANKING_COLUMN_COUNT = 'COUNT'
RANKING_CSV_FILE_PATH = 'ranking.csv'


class CsvModel(object):
    """Base csv model."""

    def __init__(self, csv_file):
        self.csv_file = csv_file
        if not os.path.exists(csv_file):
            pathlib.Path(csv_file).touch()


# csv_fileってのか無かったら作ってね

class RankingModel(CsvModel):
    """Definition of class that generates ranking model to write to CSV"""

    def __init__(self, csv_file=None, *args, **kwargs):
        if not csv_file:
            csv_file = self.get_csv_file_path()
        super().__init__(csv_file, *args, **kwargs)
        # *args: 複数の引数をタプルとして受け取る
        # **kwargs: 複数のキーワード引数を辞書として受け取る
        self.column = [RANKING_COLUMN_FOOD_NAME, RANKING_COLUMN_COUNT]
        self.data = collections.defaultdict(int)
        # valuにint型が入るdictt型の変数data
        self.load_data()

    def get_csv_file_path(self):
        """Set csv file path.

        Use csv path if set in settings, otherwise use default
        """

        csv_file_path = None
        try:
            import settings
            if settings.CSV_FILE_PATH:
                csv_file_path = settings.CSV_FILE_PATH
        except ImportError:
            pass
        # settings.pyにcsv pathがあったら使ってね。無い時は無いよって言うエラー出してね。
        if not csv_file_path:
            csv_file_path = RANKING_CSV_FILE_PATH
        return csv_file_path

    # 変数csv_file_pathがなければ、最初に定義しているグローバル関数RANKING_CSV_FILE_PATHをcsv_file_pathに代入して、返り値にします。#

    def load_data(self):
        """Load csv data.
        Returns:
            dict: Returns ranking data of dict type.
        """
        with open(self.csv_file, 'r+') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.data[row[RANKING_COLUMN_FOOD_NAME]] = int(
                    row[RANKING_COLUMN_COUNT])
        return self.data

    def save(self):
        """Save data to csv file."""
        with open(self.csv_file, 'w+') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.column)
            writer.writeheader()

            for food_name, count in self.data.items():
                writer.writerow({
                    RANKING_COLUMN_FOOD_NAME: food_name,
                    RANKING_COLUMN_COUNT: count
                })

    def get_most_popular(self, not_list=None):
        """Fetch the data of the top most ranking.

        Args:
            not_list (list): Excludes the name on the list.

        Returns:
            str: Returns the data of the top most ranking
        """
        if not_list is None:
            not_list = []

        if not self.data:
            return None

        sorted_data = sorted(self.data, key=self.data.get, reverse=True)
        for food_name in sorted_data:
            if food_name in not_list:
                continue
            return food_name

    def increment(self, food_name):
        """Increase rank for the give name."""
        self.data[food_name.title()] += 1
        self.save()