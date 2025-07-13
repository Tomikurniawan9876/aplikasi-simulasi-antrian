import streamlit as st

def queue_simulation(lambda_rate, mu_rate):
    rho = lambda_rate / mu_rate
    if rho >= 1:
        return None, "Sistem tidak stabil (ρ >= 1)"
    
    L = rho / (1 - rho)
    Lq = rho**2 / (1 - rho)
    W = 1 / (mu_rate - lambda_rate)
    Wq = rho / (mu_rate - lambda_rate)
    
    result = {
        'Utilisasi (ρ)': rho,
        'Rata-rata pelanggan dalam sistem (L)': L,
        'Rata-rata pelanggan dalam antrian (Lq)': Lq,
        'Rata-rata waktu dalam sistem (W)': W,
        'Rata-rata waktu tunggu dalam antrian (Wq)': Wq
    }
    return result, None

st.title("📊 Simulasi Antrian M/M/1 (Queueing Model)")

lambda_rate = st.number_input("λ - Rata-rata kedatangan", min_value=0.01, value=1.0)
mu_rate = st.number_input("μ - Rata-rata pelayanan", min_value=0.01, value=2.0)

if st.button("Hitung"):
    hasil, error = queue_simulation(lambda_rate, mu_rate)
    if error:
        st.error(error)
    else:
        st.success("Hasil Simulasi:")
        for k, v in hasil.items():
            st.write(f"**{k}**: {v:.4f}")
