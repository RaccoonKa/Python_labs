import csv
import os
import random


class TitanicDataProcessor:
    def __init__(self):
        self.data = []

    def load_data(self):
        with open('Titanic.csv', 'r') as file:
            csv_reader = csv.reader(file)
            self.data = [row for row in csv_reader]

    def show(self, display_type='top', num_rows=5, separator=','):
        if display_type == 'top':
            rows = self.data[:num_rows]
        elif display_type == 'bottom':
            rows = self.data[-num_rows:]
        elif display_type == 'random':
            rows = random.sample(self.data, num_rows)
        else:
            print('Invalid display type')
            return

        for row in rows:
            print(separator.join(row))

    def info(self):
        print(f'{len(self.data) - 1}x{len(self.data[0])}')

        headers = self.data[0]
        for col_idx, header in enumerate(headers):
            non_empty_count = sum(1 for row in self.data[1:] if row[col_idx])
            col_type = type(self.data[1][col_idx]).__name__
            print(f'{header} {non_empty_count} {col_type}')

    def del_nan(self):
        self.data = [row for row in self.data if all(row)]

    def make_ds(self):
        random.shuffle(self.data)
        split_idx = int(0.7 * len(self.data))

        learning_data = self.data[:split_idx]
        testing_data = self.data[split_idx:]

        os.makedirs('workdata/Learning', exist_ok=True)
        os.makedirs('workdata/Testing', exist_ok=True)

        with open('workdata/Learning/train.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(learning_data)

        with open('workdata/Testing/test.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(testing_data)


titanic_processor = TitanicDataProcessor()
titanic_processor.load_data()
titanic_processor.show(display_type='top', num_rows=5)
titanic_processor.info()
titanic_processor.del_nan()
titanic_processor.make_ds()
