import pandas as pd
import math
data_dt = pd.read_excel("DatasetGiaDT.xlsx")
[n,m] = data_dt.shape
MinRam = min(data_dt.Ram)
MinRom = min(data_dt.Rom)
MinWeight = min(data_dt.Weight)
MinScreen = min(data_dt.Screen)
MinPin = min(data_dt.Pin)
MinWidth = min(data_dt.Width)
MinHeight = min(data_dt.Height)
MinGia = min(data_dt.Price)
MaxRam = max(data_dt.Ram)
MaxRom = max(data_dt.Rom)
MaxWeight = max(data_dt.Weight)
MaxScreen = max(data_dt.Screen)
MaxPin = max(data_dt.Pin)
MaxWidth = max(data_dt.Width)
MaxHeight = max(data_dt.Height)
MaxGia = max(data_dt.Price)
def ChuanHoa(x, minn, maxx):
    return (x-minn)/(maxx-minn)
DSDT = []
DSDTChuanHoa = []
for i in range(n):
    Pk = 1 if data_dt.Phan_Khuc[i] == "Flagship" else 2 if data_dt.Phan_Khuc[i] == "Cận cao cấp" else 3 if data_dt.Phan_Khuc[i] == "Tầm trung" else 4
    DSDT.append((data_dt.TenSP[i],data_dt.Hang[i],data_dt.Ram[i],data_dt.Rom[i],
        data_dt.Weight[i],data_dt.Screen[i],data_dt.Pin[i],data_dt.Width[i],
        data_dt.Height[i], data_dt.CPU[i],data_dt.Sceen_Quality[i],data_dt.Price[i],Pk))
    DSDTChuanHoa.append((data_dt.Hang[i],ChuanHoa(data_dt.Ram[i],MinRam,MaxRam)
        ,ChuanHoa(data_dt.Rom[i],MinRom,MaxRom),ChuanHoa(data_dt.Weight[i],MinWeight,MaxWeight)
        ,ChuanHoa(data_dt.Screen[i],MinScreen,MaxScreen),ChuanHoa(data_dt.Pin[i],MinPin,MaxPin)
        ,ChuanHoa(data_dt.Width[i],MinWidth,MaxWidth),ChuanHoa(data_dt.Height[i],MinHeight,MaxHeight)
        , data_dt.CPU[i],data_dt.Sceen_Quality[i],ChuanHoa(data_dt.Price[i],MinGia,MaxGia)))

#thuật toán KNN
def KiemTraDLHopLe(DienThoaiCH):
    for i in range(len(DienThoaiCH)):
        if DienThoaiCH[i] <0 or DienThoaiCH[i] > 1:
            print("Dữ liệu đầu vào lớn hơn mức min max hiện tại!!!(cột "+str(i)+")")  
            return False 
    return True

def LayKhoangGia(LisSX,loai,k):
    j =0
    while LisSX[j][12]!= loai:
        j+=1
    maxx = LisSX[j][11]
    minn = LisSX[j][11]
    sl = 1
    for i in range(j+1,int(k),1):
        if LisSX[i][12] == loai:
            sl+=1
            minn = LisSX[i][11] if minn > LisSX[i][11] else minn
            maxx = LisSX[i][11] if maxx < LisSX[i][11] else maxx
            if sl == 2:
                break
    return str(minn) +" --> "+ str(maxx) +"VNĐ"
def TinhKhoangCach2(x,y):
    tong=0
    for i in range(len(x)):
        tong+=((x[i]-y[i])**2)
    return tong ** (1/2)
def DiemDangChuan2(i):
    return ((i[1],ChuanHoa(i[2],MinRam,MaxRam),ChuanHoa(i[3],MinRom,MaxRom)
            ,ChuanHoa(i[4],MinWeight,MaxWeight),ChuanHoa(i[5],MinScreen,MaxScreen)
            ,ChuanHoa(i[6],MinPin,MaxPin),ChuanHoa(i[7],MinWidth,MaxWidth)
            ,ChuanHoa(i[8],MinHeight,MaxHeight),i[9],i[10]))
def LayDSChuan2(DSDT):
    DSChuan = []
    for i in DSDT:
        DSChuan.append(DiemDangChuan2(i))
    return DSChuan
def PhanKhuc(loai):
    return "Flagship" if loai == 1 else "Cận cao cấp" if loai == 2 else "Tầm trung" if loai == 3 else "Giá rẻ"
class KhoangCach:
    def __init__(self,kc,index) -> None:
        self.KhoangCach = kc
        self.index = index
def TinhK(DSDT):
    loais = [0]*4
    for item in DSDT:
        loais[item[12] -1]+=1 
    return int(min(loais)/2+1)
    
def KNN(DSDT,dt):
    DSChuan2=LayDSChuan2(DSDT)
    ListKC = []
    LisSX = []
    for i in range(len(DSChuan2)):
        Kc = KhoangCach(TinhKhoangCach2(DSChuan2[i],dt),i)
        j = 0
        KC_len = len(ListKC)
        while KC_len>j and Kc.KhoangCach >ListKC[j].KhoangCach :
            j+=1
        ListKC.insert(j,Kc)
        LisSX.insert(j,DSDT[i])
    k = TinhK(DSDT)
    Loais = [0]*4
    mx = 0
    for i in range(k):
        Loais[DSDT[ListKC[i].index][12]-1]+=1
        mx = DSDT[ListKC[i].index][12]-1 if Loais[mx] < Loais[DSDT[ListKC[i].index][12]-1] else mx            
    print("Giá dự kiến: ",LayKhoangGia(LisSX,mx+1,k))
    return mx+1    
# ten = "SamSunghihi"
# hang = 0.8
# ram = 12
# rom = 256
# weight = 190
# sreeen = 6.5
# pin = 4000
# width = 77
# height = 165
# cpu = 0.7
# sceen_quality = 0.6

# ten = "SamSunghihi"
# hang = 0.1
# ram = 6
# rom = 256
# weight = 167
# sreeen = 6.1
# pin = 3500
# width = 71.8
# height = 151.9
# cpu = 0.4
# sceen_quality = 0.6

# ten = "SamSunghihi"
# hang = 0.2
# ram = 1
# rom = 32
# weight = 130
# sreeen = 5.5
# pin = 1820
# width = 68
# height = 140
# cpu = 0.2
# sceen_quality = 0.6

ten = "Vivo V20 128gb"
hang = 0.2
ram = 8
rom = 128
weight = 171
sreeen = 6.44
pin = 4000
width = 74.2
height = 161.3
cpu = 0.6
sceen_quality = 0.8

# ten = "Samsung Galaxy Note 10+"
# hang = 0.5
# ram = 12
# rom = 256
# weight = 190
# sreeen = 6.7
# pin = 4300
# width = 77.2
# height = 162.3
# cpu = 0.8
# sceen_quality = 0.9

# ten = "Xiaomi10"
# hang = 0.5
# ram = 12
# rom = 256
# weight = 190
# sreeen = 6.7
# pin = 4300
# width = 77.2
# height = 162.3
# cpu = 0.8
# sceen_quality = 0.9

# ten = "iphone 13 pro max"
# hang = 0.9
# ram = 6
# rom = 1024
# weight = 240
# sreeen = 6.7
# pin = 4352
# width = 78.1
# height = 160.8
# cpu = 0.95
# sceen_quality = 0.8

DienThoai = (ten,hang,ram,rom,weight,sreeen,pin,width,height,cpu,sceen_quality)
DienThoaiCH = DiemDangChuan2(DienThoai) 
if KiemTraDLHopLe(DienThoaiCH) == True:
    print("Dự đoán giá của điện thoại "+DienThoai[0]+":")
    loai = KNN(DSDT,DienThoaiCH)
    print("Phân khúc: ",PhanKhuc(loai))
