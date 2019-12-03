import functions
from app.main.DB import DB
from app.main.Weather import get_max_min_weekly_weather
import pymysql
import pandas as pd


import time

global user_info
global mission_info
global classified_R_hat

def set_R_hat():
    DB.dbConnect()
    DB.setCursorDic()

    global user_info
    global mission_info
    global classified_R_hat

    weather_category = ['sunny', 'cloudy', 'rainy','snowy']
    '''
    유저와 관련된 정보들 가져오기
    '''
    sql = "SELECT userIndex as user_id,1 as time_min, time_affordable as time_max, expense_affordable as cost,NULL as applicable_missions, NULL as weekly_missions FROM User"
    try:
        DB.curs.execute(sql)
        user_list_db = DB.curs.fetchall()
    except pymysql.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))

    user_info = pd.DataFrame(data=user_list_db,
                             columns=['user_id', 'time_min', 'time_max', 'cost', 'applicable_missions',
                                      'weekly_missions'])
    user_info.set_index('user_id', inplace=True, drop=True)

    weather_category = ['sunny', 'cloudy', 'rainy', 'snowy']

    '''
        미션과 관련된 정보들 불러오기
        '''
    sql = "SELECT missionID as mission_id, missionTime as time, expense as cost FROM Mission"
    try:
        DB.curs.execute(sql)
        mission_list_db = DB.curs.fetchall()
    except pymysql.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
    '''
    mission_info = pd.DataFrame(data=mission_list_db, columns=['mission_id', 'time', 'cost'])
    mission_info.set_index('mission_id', inplace=True)

    temperature_dic = get_max_min_weekly_weather()
    temperature_min = int(temperature_dic['min'])
    temperature_max = int(temperature_dic['max'])

    R_user_id = list(mission_evaluation_df.loc[:, 'user'])
    R_mission_id = list(mission_evaluation_df.loc[:, 'mission'])
    R_weather = list(mission_evaluation_df.loc[:, 'weather'])
    R_temperature = list(mission_evaluation_df.loc[:, 'temperature'])
    R_rating = list(mission_evaluation_df.loc[:, 'rating'])
    R_data_num = _cnt['cnt']

    R_user_id = list(mission_evaluation_df.loc[:, 'user'])
    R_mission_id = list(mission_evaluation_df.loc[:, 'mission'])
    R_weather = list(mission_evaluation_df.loc[:, 'weather'])
    R_temperature = list(mission_evaluation_df.loc[:, 'temperature'])
    R_rating = list(mission_evaluation_df.loc[:, 'rating'])
    R_data_num = _cnt['cnt']

    



    log = functions.get_init_log(weather_category, user_info.index, mission_info.index)

    classified_R = functions.get_classified_R(user_info.index, mission_info.index, weather_category, temperature_min, temperature_max, R_user_id, R_mission_id, R_weather, R_temperature, R_rating, R_data_num)

    start1 = time.time()

    classified_R_hat = functions.get_classified_R_hat_by_KNN(classified_R, log)
    #classified_R_hat = get_classified_R_hat_by_Regression(classified_R)
    #classified_R_hat = get_classified_R_hat_by_matrix_completion(classified_R)

    print(time.time() - start1)
    '''
    return


def function():
    global user_info
    global mission_info
    global classified_R_hat

    user_info = "가나다라"
    return

def printaa():
    print(user_info)

    return