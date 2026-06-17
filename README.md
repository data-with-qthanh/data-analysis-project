# 📊 Data Analysis Project — Vietnam Sales 2024

Dự án phân tích dữ liệu bán hàng Việt Nam 2024 dành cho người mới bắt đầu học Data Analysis.

## 🎯 Mục tiêu
- Làm quen với quy trình phân tích dữ liệu thực tế (EDA)
- Thực hành với Pandas, Matplotlib, Seaborn
- Rèn kỹ năng trực quan hóa dữ liệu

## 🛠 Công nghệ sử dụng
| Thư viện | Mục đích |
|----------|----------|
| `pandas` | Xử lý & phân tích dữ liệu |
| `numpy` | Tính toán số học |
| `matplotlib` | Vẽ biểu đồ cơ bản |
| `seaborn` | Vẽ biểu đồ thống kê đẹp |
| `jupyter` | Môi trường notebook |

## 📁 Cấu trúc thư mục
```
data-analysis-project/
├── data/
│   ├── raw/              ← Dữ liệu gốc (không chỉnh sửa)
│   └── processed/        ← Dữ liệu sau khi làm sạch
├── notebooks/
│   └── 01_eda.ipynb      ← Notebook phân tích chính
├── src/                  ← Python modules tái sử dụng
├── outputs/              ← Biểu đồ & kết quả xuất ra
├── requirements.txt
└── README.md
```

## 🚀 Cách chạy

### 1. Clone repo
```bash
git clone https://github.com/TEN_BAN/data-analysis-project.git
cd data-analysis-project
```

### 2. Cài thư viện
```bash
pip install -r requirements.txt
```

### 3. Mở Jupyter Notebook
```bash
jupyter notebook
```
Sau đó mở file `notebooks/01_eda.ipynb` và chạy từng cell.

## 📈 Kết quả phân tích

- **Doanh thu theo tháng** — xu hướng tăng trưởng cả năm
- **Top thành phố** — so sánh hiệu suất theo địa lý
- **Danh mục sản phẩm** — tỷ trọng và hiệu suất từng ngành hàng
- **Rating khách hàng** — phân phối và mức độ hài lòng
- **Heatmap** — tương quan thành phố × danh mục

## 👤 Tác giả
- GitHub: [@TEN_BAN](https://github.com/TEN_BAN)
