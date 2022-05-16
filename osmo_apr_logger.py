import requests
import json
import pandas as pd
import os
from datetime import date

def get_name_by_id(id):
    # get pool name(SYM/SYM2) by id

    pair_summary_url = R'https://api-osmosis.imperator.co/pairs/v1/summary'
    pair_response = requests.get(pair_summary_url)
    pair_json = json.loads(pair_response.content)
    for row in pair_json['data']:
        pool_summary_id = int(row['pool_id'])
        if int(id) == pool_summary_id:
            base_sym = row['base_symbol']
            quote_sym = row['quote_symbol']
            name = f'{base_sym}_{quote_sym}'
            return name
    


def update_log(update_status):
    today = date.today()
    today_log_path = f"< insert file path here > \\OSMO_apr_data\\logs\\{today}.txt" ### ADD RELEVANT PATH
    if not os.path.exists(today_log_path):
        open(today_log_path, 'w')

    with open(today_log_path, 'a') as day_log:
        day_log.write(f'{update_status}\n')


url = R'https://api-osmosis.imperator.co/apr/v2/all'

response = requests.get(url=url)
all_pools = json.loads(response.content)

#create and update pool csv 
for row in all_pools:

    pool_name_by_symbol = get_name_by_id(row['pool_id'])
    today = date.today()
    apr_list = [today, row['apr_list'][0]['apr_1d'], row['apr_list'][0]['apr_7d'], row['apr_list'][0]['apr_14d']]
    file_path = f"< insert file path here > \\OSMO_apr_data\\pool_info\\{pool_name_by_symbol}.csv"  ###  ADD RELEVANT PATH


    if not os.path.exists(file_path):

        try:
            pool_info_by_id = pd.DataFrame([apr_list], columns=('day', '1 day unbonding', '7 day unbonding', '14 day unbonding'))
            pool_info_by_id.to_csv(file_path, na_rep=0,  index=False)
            update_log(f'converted to csv: {pool_name_by_symbol}')
        except:
            
            update_log(f'conversion failed: {pool_name_by_symbol}')

    else:
        try:   
            pool_info_by_id = pd.DataFrame([apr_list])
            pool_info_by_id.to_csv(file_path, na_rep=0, mode='a', index=False, header=False)
            update_log(f'updated csv: {pool_name_by_symbol}')

        except:
            update_log(f'update failed: {pool_name_by_symbol}')