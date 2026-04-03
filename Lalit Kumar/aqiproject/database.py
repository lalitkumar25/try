

import sqlite3
from datetime import datetime


DB_NAME = "aqi_data.db"


def get_db():
    try:
        
        conn = sqlite3.connect(DB_NAME)
        
        conn.row_factory = sqlite3.Row
        return conn
    except Exception as e:
        print("DB Connection Error:", e)
        return None


def init_db():
    conn = get_db()
    if conn:
        try:
            cursor = conn.cursor()
           
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    city TEXT,
                    aqi INTEGER,
                    date_time TEXT
                )
            ''')
            conn.commit()
            print("Database ready.")
        except Exception as e:
            print("Error creating table:", e)
        finally:
            conn.close()


def save_search(city, aqi):
    conn = get_db()
    if conn:
        try:
            cursor = conn.cursor()
            
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  #date today
            
            
            cursor.execute("INSERT INTO history (city, aqi, date_time) VALUES (?, ?, ?)", (city, aqi, now)) #data insert
            conn.commit()
            print(f"Saved: {city} (AQI: {aqi})")
        except Exception as e:
            print("Save failed:", e)
        finally:
            conn.close()

# recent 10 records 
def get_recent_data():
    conn = get_db()
    result = []
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT city, aqi, date_time FROM history ORDER BY id DESC LIMIT 10")
            rows = cursor.fetchall()
            
            
            for row in rows:
                result.append({
                    "city": row["city"],
                    "aqi": row["aqi"],
                    "date": row["date_time"] # data to list
                })
        except:
            pass
        finally:
            conn.close()
    return result


def get_all_data():
    conn = get_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT city, aqi, date_time FROM history ORDER BY id DESC")# dawnload 
            return cursor.fetchall()
        except:
            return []
        finally:
            conn.close()
    return []