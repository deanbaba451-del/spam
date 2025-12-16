import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

async def create_session():
    # API bilgilerinizi girin
    API_ID = int(input("38400691
(my.telegram.org'dan alın): "))
    API_HASH = input("a5105958d8b2a502b77d823cab0e7646 (my.telegram.org'dan alın): ")
    
    # Client oluştur
    client = TelegramClient(StringSession(), API_ID, API_HASH)
    
    try:
        # Bağlan
        await client.start()
        
        # Session string al
        session_str = client.session.save()
        
        print("\n" + "="*60)
        print("✅ SESSION STRING (Bu kopyalayıp kaydedin):")
        print("="*60)
        print(session_str)
        print("="*60)
        
        # Dosyaya kaydet
        with open("session.txt", "w", encoding="utf-8") as f:
            f.write(session_str)
        print("\n✅ Session string 'session.txt' dosyasına kaydedildi")
        
        return session_str
        
    finally:
        await client.disconnect()

# Async fonksiyonu çalıştır
def main():
    print("="*50)
    print("TELEGRAM SESSION OLUŞTURUCU")
    print("="*50)
    
    try:
        session = asyncio.run(create_session())
        print("\n✅ Session başarıyla oluşturuldu!")
        print(f"Session: {session}")
        
    except KeyboardInterrupt:
        print("\n❌ İşlem kullanıcı tarafından durduruldu")
    except Exception as e:
        print(f"\n❌ Hata oluştu: {e}")

if __name__ == "__main__":
    main()
