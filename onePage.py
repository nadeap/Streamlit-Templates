import numpy as np
import pickle
import streamlit as st  

model = pickle.load(open('model.pkl','rb'))

def ipm_predict(input_data):
    
    id_np_array = np.asarray(input_data)
    id_reshaped = id_np_array.reshape(1,-1)

    prediction = model.predict(id_reshaped)
    print(prediction)

    if(prediction[0]==0):
        return "Hasil: Jawaban"
    elif(prediction[0]==1):
        return "Hasil: Jawaban"
    else:
        return "Hasil: Jawaban"
    
def main():
    
    st.title('JUDUL WEB')
    
    Harapan_Lama_Sekolah = st.text_input('Harapan Lama Sekolah')
    Pengeluaran_Perkapita = st.text_input('Pengeluaran Perkapita')
    Rerata_Lama_Sekolah = st.text_input('Rerata Lama Sekolah')
    Usia_Harapan_Hidup = st.text_input('Usia Harapan Hidup')
    
    prediksi = ''
    
    if st.button('PREDICT'):
        prediksi = ipm_predict([Harapan_Lama_Sekolah, Pengeluaran_Perkapita, Rerata_Lama_Sekolah, Usia_Harapan_Hidup])
        
    st.success(prediksi)
    
if __name__=='__main__':
    main()