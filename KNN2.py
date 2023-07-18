import pandas as pd
import random
import copy 
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


def DiemDangChuan(i):
    return ((i[1],ChuanHoa(i[2],MinRam,MaxRam),ChuanHoa(i[3],MinRom,MaxRom)
            ,ChuanHoa(i[4],MinWeight,MaxWeight),ChuanHoa(i[5],MinScreen,MaxScreen)
            ,ChuanHoa(i[6],MinPin,MaxPin),ChuanHoa(i[7],MinWidth,MaxWidth)
            ,ChuanHoa(i[8],MinHeight,MaxHeight),i[9],i[10],ChuanHoa(i[11],MinGia,MaxGia)))

def LayChuanHoa(DSBT):
    DSCH = []
    for i in DSBT:
        DSCH.append(DiemDangChuan(i))
    return DSCH

def TinhKhoangCachHaiDiem(x,y):
    return math.dist(x,y)
def TinhKhoangCachTuMotDiem(DSDT , diem):
    DSKC = []
    for item in DSDT:
        DSKC.append(TinhKhoangCachHaiDiem(diem,item))
    return DSKC

class PhanKhucDienThoai:
    def __init__(self, TenPK,DSDT):
        self.TePK = TenPK
        self.DSDT = DSDT
        self.DSDTChuanHoa = LayChuanHoa(DSDT)
        minn = DSDT[0][11]
        maxx = DSDT[0][11]
        hangTB = 0
        ramTB = 0
        romTB = 0
        weightTB = 0
        screenTB = 0
        pinTB = 0
        widthTB = 0
        heightTB = 0
        cpuTB = 0
        sceenQualityTB = 0
        tonggia = DSDT[0][11]
        sll = len(DSDT)
        for i in range(1,sll,1):
            minn = DSDT[i][11] if minn > DSDT[i][11] else minn
            maxx = DSDT[i][11] if maxx < DSDT[i][11] else maxx
            tonggia+=DSDT[i][11]
            hangTB +=DSDT[i][1]
            ramTB +=DSDT[i][2]
            romTB +=DSDT[i][3]
            weightTB +=DSDT[i][4]
            screenTB +=DSDT[i][5]
            pinTB +=DSDT[i][6]
            widthTB +=DSDT[i][7]
            heightTB +=DSDT[i][8]
            cpuTB +=DSDT[i][9]
            sceenQualityTB +=DSDT[i][10]
        self.GiaMin = minn
        self.GiaMax = maxx
        self.GiaTrungBinh = int(tonggia/sll)
        self.HangTB = hangTB/sll
        self.RamTB = int(ramTB/sll)
        self.RomTB = int(romTB/sll)
        self.WeightTB = int(weightTB/sll)
        self.ScreenTB = int(screenTB/sll)
        self.PinTB = int(pinTB/sll)
        self.WidthTB = int(widthTB/sll)
        self.HeightTB = int(heightTB/sll)
        self.CPUTB = cpuTB/sll
        self.SceenQualityTB = sceenQualityTB/sll
        self.TongSL = sll
    def Xuat(self):
        print(self.TePK)
        print("Hang: "+str(self.HangTB))
        print("Ram: "+str(self.RamTB))
        print("Rom: "+str(self.RomTB))
        print("Weight: "+str(self.WeightTB))
        print("Screen: "+str(self.ScreenTB))
        print("Pin: "+str(self.PinTB))
        print("Width: "+str(self.WidthTB))
        print("Height: "+str(self.HeightTB))
        print("CPU: "+str(self.CPUTB))
        print("Sceen_Quality: "+str(self.SceenQualityTB))
        print("Gia trung bình: "+str(self.GiaTrungBinh) +" VNĐ")
        print("Tổng số lượng: "+str(self.TongSL))
        print()

def CheckThayDoi(Truoc, Sau):
    for i in range(len(Truoc)):
        if Truoc[i] != Sau[i]:
            return False
    return True
def CheckThayDoiCum(CumT, CumS):
    for i in range(len(CumT)):
        if CumT[i] !=CumS[i]:
            return False
    return True

def TinhToaDoTam(Cum):
    sl = len(Cum)
    tammoi = []
    for i in range(len(Cum[0])):
        tong = 0
        for j in range(sl):
            tong += Cum[j][i]
        tammoi.append(tong/sl)
    return tuple(tammoi)

def XuatTam(Tams):
    for i in Tams:
        print(i)

def TimTamGanNhat(item, Tams):
    minn = 0
    m = TinhKhoangCachHaiDiem(Tams[minn],item)
    for i in range(1,len(Tams),1):
        KC = TinhKhoangCachHaiDiem(Tams[i],item)
        minn = i if m > KC else minn
        m = KC if m>KC else KC
    return minn
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
        loais[item[12]-1]+=1
    return int(min(loais)/2)
def K_means(DSDT,DSDTChuanHoa, Tams):
    sl = len(Tams)
    Cums =  []
    lanlap = 0
    cum1 = []
    cum2 = []
    cum3 = []
    cum4 = []
    ccum1 = []
    ccum2 = []
    ccum3 = []
    ccum4 = []
    while lanlap < 2 or Cumt!=Cums:
        lanlap+=1
        Cumt = copy.deepcopy(Cums)      
        Cums.clear()
        Cums =[]
        cum1.clear()
        cum2.clear()
        cum3.clear()
        cum4.clear()
        cum1 = []
        cum2 = []
        cum3 = []
        cum4 = []
        ccum1.clear()
        ccum2.clear()
        ccum3.clear()
        ccum4.clear()
        ccum1 = []
        ccum2 = []
        ccum3 = []
        ccum4 = []
        for j in range(len(DSDTChuanHoa)):
            minn = 0
            for i in range(1,sl,1):
                KC = TinhKhoangCachHaiDiem(Tams[i],DSDTChuanHoa[j])
                minn = i if TinhKhoangCachHaiDiem(Tams[minn],DSDTChuanHoa[j]) > KC else minn
            if minn ==0:
                cum1.append(DSDTChuanHoa[j])
                ccum1.append(DSDT[j])
            elif minn ==1:
                cum2.append(DSDTChuanHoa[j])
                ccum2.append(DSDT[j]) 
            elif minn ==2:
                cum3.append(DSDTChuanHoa[j])
                ccum3.append(DSDT[j]) 
            elif minn ==3:
                cum4.append(DSDTChuanHoa[j])
                ccum4.append(DSDT[j]) 
            minn = None 
        Cums.append(cum1)
        Cums.append(cum2)
        Cums.append(cum3)
        Cums.append(cum4)
        for i in cum1:
            for j in cum2:
                if i == j:
                    print("Lõi")
                    return
        Tams[0] = TinhToaDoTam(cum1)
        Tams[1] = TinhToaDoTam(cum2)
        Tams[2] = TinhToaDoTam(cum3)
        Tams[3] = TinhToaDoTam(cum4)
    KetQua = []
    KetQua.append(ccum1)
    KetQua.append(ccum2)
    KetQua.append(ccum3)
    KetQua.append(ccum4)
    return KetQua
def PhanCapTheoPhanCum(DSTheoCum, DT):
    DSCHuan2 = []
    for i in range(len(DSTheoCum)):
        DSCHuan2.append(LayDSChuan2(DSTheoCum[i]))
    ListKC =[]
    for item in DSCHuan2:
        for i in item:
            Kc = TinhKhoangCach2(i,DT)
            j = 0
            KC_len = len(ListKC)
            while KC_len>j and Kc  > TinhKhoangCach2(ListKC[j],DT):
                j+=1
            ListKC.insert(j,i)
    k = TinhK(DSDT)
    loais = [0]*4
    mx = 0
    l = 0
    for i in range(len(DSCHuan2)):        
        for j in range(len(DSCHuan2[i])):
            for t in range(k):                  
                if ListKC[t]==DSCHuan2[i][j]:
                    loais[DSTheoCum[i][j][12]-1]+=1
                    mx = DSTheoCum[i][j][12]-1 if loais[mx] < loais[DSTheoCum[i][j][12]-1] else mx
                    l+=1                
            if l == k:
                return mx+1 


#thuật toán KNN
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

# ten = "Vivo V20 128gb"
# hang = 0.2
# ram = 8
# rom = 128
# weight = 171
# sreeen = 6.44
# pin = 4000
# width = 74.2
# height = 161.3
# cpu = 0.6
# sceen_quality = 0.8

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

# ten = "Xiaomi Mi Note 10"
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
# if KiemTraDLHopLe(DienThoaiCH) == True:
#     loai = KNN(DSDT,DienThoaiCH)
#     print("Phân khúc: ",PhanKhuc(loai))

        # index_ran = random.sample(range(n), 4)
# phân cấp điện thoại theo cụm được phân cụm bằng K mean:
Tams = []
indexs = [130, 165, 69, 95]
for i in range(4):
    Tams.append(DSDTChuanHoa[indexs[i]])
KetQua = K_means(DSDT,DSDTChuanHoa,Tams)
PhanKhuc = []
ii = 0
for i in KetQua:
    ii+=1
    PhanKhuc.append(PhanKhucDienThoai("Phân khúc "+str(ii),i))

for item in PhanKhuc:
    item.Xuat()
l = PhanCapTheoPhanCum(KetQua,DienThoaiCH)
print("Điện thoại này thuộc phân khúc: ",l)

