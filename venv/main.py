import pandas as pd


df = pd.read_excel("general_hospital_data.xlsx")
# excel dosyası okumak için 
#

# İsimleri düzelt (baş harf büyük)
df["Patient Name"] = df["Patient Name"].str.strip().str.title()


df["Gender"] = df["Gender"].str.strip().str.title()
# cinsiyet verileri için
df["Region"] = df["Region"].str.strip().str.title()
#yaşadıkları bölgeler
df["Medical Condition"] = df["Medical Condition"].str.strip().str.title()

# Tarih formatı
df["Date of Admission"] = pd.to_datetime(df["Date of Admission"])
df["Date of Discharge"] = pd.to_datetime(df["Date of Discharge"])



df["Length_of_Stay"] = (df["Date of Discharge"] - df["Date of Admission"]).dt.days
#hastanede kaldığı süreyi bulmak içiin çıkış tarihinden çıkış tarihini çıkarttık yeni bir veri oluşturup oraya atadık
# ------------------------


df["Survival_Status"] = df["Outcome"].apply(
    lambda x: 1 if x == "Success" else 0
)
#veri üzezerinde daha iyi çaışma yapmak için binary yaptım

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

# yeni excel dosyası 

df.to_excel("YeniHastaneVerisi.xlsx", index=False)

print("İşlem tamamlandı, temizlenmiş veri oluştu")