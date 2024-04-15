"""prompt
請編寫一個用於讀取每天降雨量的程式，若出現降雨量為負值則應該排除，因為不可能發生。
輸出的結果中要包含有效紀錄天數，雨天數，期間的總降雨量，以及單日最大降雨量是哪天。
並使用9999作為終止程式的哨兵值(sentinel value，或稱為信號值)。
"""
def calculate_rainfall():
    valid_records = 0
    rainy_days = 0
    total_rainfall = 0
    max_rainfall = 0
    max_rainfall_day = None

    while True:
        rainfall = float(input("Enter the rainfall amount (9999 to quit): "))
        
        if rainfall == 9999:
            break
        
        if rainfall < 0:
            continue
        
        valid_records += 1
        total_rainfall += rainfall
        rainy_days += 1
        
        if rainfall > max_rainfall:
            max_rainfall = rainfall
            max_rainfall_day = valid_records
    
    print("Valid records: ", valid_records)
    print("Rainy days: ", rainy_days)
    print("Total rainfall: ", total_rainfall)
    print("Day with maximum rainfall: ", max_rainfall_day)

calculate_rainfall()