"""
Modul Tools — fungsi-fungsi "aksi" yang dipanggil router ketika intent
BUKAN pertanyaan informasi/kebijakan, melainkan permintaan spesifik
yang butuh pengecekan data langsung (bukan retrieval semantik).

Pola ini mengikuti konsep Tool Integration di Sesi 12.3.
"""

import pandas as pd

MOCK_TICKETS_PATH = "data/mock_tickets.csv"


def get_ticket_status(ticket_id: str) -> dict:
    """
    Mencari status tiket berdasarkan ticket_id pada data mock_tickets.csv.

    # TODO: implementasikan pencarian data tiket berdasarkan ticket_id.
    # Jika ticket_id tidak ditemukan, kembalikan pesan yang informatif
    # (bukan error yang membuat aplikasi crash).
    #
    # Contoh langkah:
    #   1. Muat mock_tickets.csv menggunakan pandas
    #   2. Cari baris dengan ticket_id yang cocok
    #   3. Jika ditemukan, susun string jawaban (subject, status, last_update)
    #   4. Jika tidak ditemukan, kembalikan pesan bahwa tiket tidak ditemukan
    """
    ticket_df = pd.read_csv(MOCK_TICKETS_PATH)
    found_ticket_df = ticket_df.loc[ticket_df['ticket_id'] == ticket_id]

    if len(found_ticket_df) == 0:
        return {"status":"error", "data":f"Tiket {ticket_id} tidak ditemukan"}
    else:
        message_returned = f"Tiket {ticket_id}"
        for _, found_ticket in found_ticket_df.iterrows():
            message_returned += f"{'-'*12}"
            message_returned += f"\nSubject: {found_ticket['subject']}\nStatus: {found_ticket['status']}\nLast update: {found_ticket['last_update']}"
            message_returned += f"{'-'*12}"
        return {"status":"success", "data":message_returned}
