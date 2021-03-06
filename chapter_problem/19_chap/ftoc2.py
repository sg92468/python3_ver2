F_BOIL_TEMP = 212.0
F_FRREEZE_TEMP = 32.0
C_BOIL_TEMP = 100.0
C_FREEZE_TEMP = 0.0
F_RAMGE = F_BOIL_TEMP - F_FRREEZE_TEMP
C_RANGE = C_BOIL_TEMP - C_FREEZE_TEMP
F_C_RATIO = C_RANGE / F_RAMGE
def ftoc(f_temp):
    """華氏の温度<f_temp>をを摂氏に変換して返す"""
    c_temp = (f_temp - F_FRREEZE_TEMP) * F_C_RATIO + C_FREEZE_TEMP
    return c_temp

if __name__ == '__main__':
    for f_temp in [-40.0, 0.0, 32.0, 100.0, 212.0]:
        c_temp = ftoc(f_temp)
        print(f'{f_temp} F => {c_temp} C')
