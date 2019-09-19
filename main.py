# /usr/env/bin python3
# -*- Coding: utf-8 -*-

import re
import pandas as pd

TEXT_PAHT = './log.txt'


def main():
    iter_flag = False

    df = pd.DataFrame(index=[], columns=['iter', 'mse_loss', 'soft_loss'])
    with open(TEXT_PAHT) as f:
        for i, line in enumerate(f):
            if iter_flag:
                if i == line_num + 1:
                    mse_loss = re.search(r'loss_eu\s=\s([0-9.]+)\s', line).group(1)

                if i == line_num + 2:
                    soft_loss = re.search(r'loss_soft\s=\s([0-9.]+)\s', line).group(1)
                    series = pd.Series([iter_num, mse_loss, soft_loss], index=df.columns)
                    df = df.append(series, ignore_index=True)
                    iter_flag = False

            m_iter = re.search(r'Iteration\s(\d+),\sTesting', line)
            if m_iter:
                iter_num = m_iter.group(1)
                iter_flag = True
                line_num = i

    df.to_csv('temp3.csv')


if __name__ == '__main__':
    main()
