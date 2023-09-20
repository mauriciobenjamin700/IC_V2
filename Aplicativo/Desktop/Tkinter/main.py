from code.extrac_features_03 import extract
from code.excel_access_04 import df_excel
from code.create_model_05 import create, save

df = extract('imagens')
df_excel(df,'FAMACHA_DATASET.xlsx')


modelo = create(excel_file='FAMACHA_DATASET.xlsx',test_size=0.1,n_estimators=100)

save(model=modelo,name_model='Modelo')