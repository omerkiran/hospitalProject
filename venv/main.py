import pandas as pd


df = pd.read_excel("general_hospital_data.xlsx")


# 1. VERİ TEMİZLEME

# isimleri düzelt (baş harfler büyük diğerleri küçük)
df["Patient Name"] = df["Patient Name"].str.strip().str.title()

# cinsiyetr verileri
df["Gender"] = df["Gender"].str.strip().str.title()

# Region temizlemek için
df["Region"] = df["Region"].str.strip().str.title()

#  sağlık durumu verilerini temizleme
df["Medical Condition"] = df["Medical Condition"].str.strip().str.title()

# Tarih formatına çevir
df["Date of Admission"] = pd.to_datetime(df["Date of Admission"])
df["Date of Discharge"] = pd.to_datetime(df["Date of Discharge"])


# 2. Yukarıya kadar olan kısım temizlem işlemiydi aşağıda veri temizlem işlemlerini yapacağız


df["Length_of_Stay"] = (df["Date of Discharge"] - df["Date of Admission"]).dt.days


# 3. hastaneden çıktığı tarihten hastaneye giriş tarihin çıkarttık ve hastanede kalış süresini hesapladık ve yeni veri olarak ekledik


df["Survival_Status"] = df["Outcome"].apply(
    lambda x: 1 if x == "Success" else 0
)


# 4. ölüm durumunu binarye çevirdik

def age_group(age):
    if age <= 18:
        return "Child"
    elif age <= 35:
        return "Young"
    elif age <= 60:
        return "Adult"
    else:
        return "Senior"

df["Age_Group"] = df["Age"].apply(age_group)


# 5. yaş kategorileri arasında analiz yapabilmek için yaşları kategorize ettik

def get_season(date):
    month = date.month
    
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"

df["Season"] = df["Date of Admission"].apply(get_season)




df.to_excel("YeniHastaneVerisi.xlsx", index=False)

print("İşlem tamamlandı. YeniHastaneVerisi.xlsx oluşturuldu.")