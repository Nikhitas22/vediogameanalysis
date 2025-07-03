
# 🎮 Video Game Sales and Engagement Analysis

This project analyzes global video game sales, user engagement, and genre trends using cleaned datasets from game metadata and regional sales records. It includes a fully interactive Power BI dashboard supported by backend data cleaning and transformation in Python with SQLite.

---

## 📁 Project Structure

```
├── cleaning.py                  # Data cleaning and merging script
├── odbc connect.py              # SQLite database connector
├── vediogames.db                # Final SQLite database with cleaned tables
├── PowerBI Dashboard.pbix       # Interactive dashboard (Power BI)
├── screenshots/                 # Saved visuals from Power BI
│   ├── top_10_games.png
│   ├── genre_sales_map.png
│   ├── wishlist_rating.png
│   ├── release_trend.png
│   └── platform_combo.png
└── README.md                    # Project overview (this file)
```

---

## 📌 Objective

To explore and uncover insights from video game data by answering:

- Which genres are most popular regionally?
- Do highly wishlisted games get better ratings?
- What’s the correlation between engagement and global sales?
- How do game ratings, backlogs, and platforms impact success?
- What are the top-performing genre-platform combinations?

---

## 🛠️ Tools & Technologies

| Tool         | Purpose                         |
|--------------|----------------------------------|
| Python (Pandas, SQLite3) | Data cleaning, transformation |
| Power BI     | Visual exploration and dashboard |
| SQLite       | Lightweight relational database  |
| DAX (Power BI) | Measures and KPIs              |

---

## 📊 Datasets Used

1. `games.csv` - Game metadata including title, genre, rating, platform, user engagement
2. `vgsales.csv` - Global and regional sales data per game

---

## 🧹 Data Cleaning Summary

Performed in `cleaning.py`:
- Handled missing/null values
- Normalized column names
- Converted data types (e.g., dates, numerics)
- Merged `games` with `vgsales` into `merged_data`
- Exported to SQLite database (`vediogames.db`)

---

## 📈 Power BI Dashboard Highlights

### ✅ Sales Analysis
- Top 10 best-selling games globally
- Year-over-year release and sales trend
- Regional heatmap: genre vs NA/EU/JP/Other sales
- Best-selling platforms and publishers

### ✅ Engagement Analysis
- Wishlist vs Rating correlation
- Plays vs Global Sales trend
- Genres with high engagement but low sales
- User rating distributions

### ✅ Categorical Comparisons
- Top-performing Genre + Platform combinations
- Backlog vs Wishlist vs Ratings
- Regional preferences by genre (heatmap & matrix)

---

## 📸 Screenshots

Here are a few captured insights from the dashboard:

| Visual Topic                  | File                           |
|------------------------------|--------------------------------|
| Top 10 Best-Selling Games    | `screenshots/top_10_games.png` |
| Wishlist vs Rating Correlation | `screenshots/wishlist_rating.png` |
| Regional Sales Heatmap       | `screenshots/genre_sales_map.png` |
| Sales Trend by Year          | `screenshots/release_trend.png` |
| Genre + Platform Performance | `screenshots/platform_combo.png` |

> *(All visuals are stored in the `screenshots/` folder)*

---

## 🤝 Author

     Nikhita  
- 💼 GitHub: Nikhitas22


---

## 📄 License

This project is for academic and portfolio use. Attribution required when reused.
