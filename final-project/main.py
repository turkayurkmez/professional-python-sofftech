import csv
import json
import os
import logging
from pathlib import Path
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("project.log"),
        logging.StreamHandler()
    ] 
)
logger = logging.getLogger(__name__)

DATA_FOLDER = Path("data")
TASKS_CSV = DATA_FOLDER / "tasks.csv"
REPORT_JSON = DATA_FOLDER/"report.json"
CSV_HEADERS = ["id","title","status","created_date"]

def setup():
    """Data klasörünü ve CSV dosyasını oluşturur."""
    try:
        DATA_FOLDER.mkdir(exist_ok=True)
        logger.info("Data klasörü oluşturuldu")

        if not TASKS_CSV.exists():
            # TODO 1: Dosya yoksa oluşturulacak!
            with open(TASKS_CSV,mode="w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f,fieldnames=CSV_HEADERS)
                writer.writeheader()
            logger.info("Görev dosyası oluşturuldu")
        else:
            logger.info("dosya zaten var")

    except OSError as e:
        logger.error(f"Ortam hazırlanırken hata oluştu. {e}")
        raise


def add_task(title:str, **extras):
    """
    CSV'ye yeni görev ekler.
    Zorunlu parametre: görev başlığı
    Opsiyonel ek alanlar (öncelik:, atanan_kisi:, status: vb)
    """
    # TODO 2: önce değerleri okumalı. O nedenle fonksiyon oluşturuyoruz.
    try:
        existing_tasks = read_tasks()
        newId = len(existing_tasks)+1
        new_task = {
            "id":newId,
            "title": title,
            "status": extras.get("status","Pending"),
            "created_date":datetime.now().strftime("%d-%m-%Y %H:%M:%S")        
        }
        
        # Tüm görevleri (eski + yeni) dosyaya yaz
        existing_tasks.append(new_task)
        
        with open(TASKS_CSV,mode="w",newline="",encoding="utf-8") as f:
            writer = csv.DictWriter(f,fieldnames=CSV_HEADERS)
            writer.writeheader()  # Başlık satırını yaz
            writer.writerows(existing_tasks)  # Tüm görevleri yaz
        
        logger.info("Yeni görev, dosyaya yazıldı")
        return new_task

    except Exception as e:
        logger.error(f"Görev eklenirken hata: {e}")
        return None

def read_tasks():
    """CSV dosyasını okur."""
    tasks = []
    try:
        if not TASKS_CSV.exists():
            return tasks
        
        with open(TASKS_CSV,mode="r",encoding="utf-8") as f:
            reader = csv.DictReader(f)  # fieldnames parametresini kaldırdık, otomatik başlık okur
            for row in reader:
                tasks.append({
                    "id":int(row["id"]),
                    "title": row["title"],
                    "status":row["status"],
                    "created_date":row["created_date"]
                })
            logger.info(f"{len(tasks)} görev okundu")
            return tasks
    except FileNotFoundError:
        logger.warning("CSV oluşturulamadı. Boş [] döndürülüyor.")
        return []
    except Exception as e:
        logger.error(f"Görev okunurken hata: {e} ")
        return []


def update_task(task_id:int, new_status:str):
    """ verilen id'li görevin durumunu günceller """
    tasks= read_tasks()
    is_updated=False
    updated = []
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            is_updated = True
            logger.info("seçilen görev güncelendi")
        updated.append(task)
    
    if not is_updated:
        logger.warning("seçilen task bulunamadı")
        raise ValueError(f"Geçersiz görev id: {task_id}")
    
    with open(TASKS_CSV,mode="w",newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
        writer.writeheader()
        writer.writerows(updated)
    
    return updated

def create_report():
    """Görevleri dosyadan okuyup json'a çevirir"""
    try:
        tasks = read_tasks()
        summary = {
            "olusturulma_tarihi":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "toplam_gorev":len(tasks),
            "durum_dagilimi":{
                status: len([t for t in tasks if t["status"]==status])
                for status in { t["status"] for t in tasks}
            },
            "gorevler":tasks

        }

        with open(REPORT_JSON,mode="w",encoding="utf-8") as f:
            json.dump(summary,f,ensure_ascii=False,indent=2)
        logger.info("JSON raporu hazır.")
        return summary
    except Exception as e:
        logger.error(f"Rapor oluşturulamadı. Hata: {e}")
        raise

def main(*titles, **settings):
    """*titles: eklenecek görevlerin başlıkları
       **settings: (örn: 'create_report': True) 
    """
    try:
        setup()
        for title in titles:
            add_task(title)
        
        tasks = read_tasks()
        if tasks:
            update_task(tasks[0]["id"],"Done")

        if settings.get('create_report',True):
            report = create_report()
            print("--- rapor özeti ---")
            print(f"Toplam görev: {report["toplam_gorev"]} ")
            for status, count in report["durum_dagilimi"].items():
                print(f"    {status}: {count}")

        logger.info("İşlem tamamlandı!")
    except Exception as e:
        logger.error(f"Hata oluştu. Detay: {e}")


if __name__ == "__main__":
    main(
        "Fast API ile REST API geliştir",
        "Unit Testleri Ekle",
        "Dokümantasyonu güncelle",
        create_report=True

    )


