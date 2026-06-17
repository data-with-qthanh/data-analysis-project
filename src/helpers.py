"""
helpers.py — Các hàm tiện ích dùng chung cho dự án
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


def load_data(path: str) -> pd.DataFrame:
    """Tải dữ liệu CSV và in thông tin cơ bản."""
    df = pd.read_csv(path)
    print(f"✅ Đã tải: {df.shape[0]} dòng x {df.shape[1]} cột")
    print(f"   Null values: {df.isnull().sum().sum()}")
    return df


def plot_bar(series: pd.Series, title: str, xlabel: str, ylabel: str,
             save_path: str = None, color: str = '#2196F3'):
    """Vẽ biểu đồ cột đơn giản."""
    fig, ax = plt.subplots(figsize=(10, 5))
    series.plot(kind='bar', ax=ax, color=color, edgecolor='white')
    ax.set_title(title, fontsize=13, fontweight='bold', pad=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"💾 Đã lưu: {save_path}")
    plt.show()


def summary_stats(df: pd.DataFrame, group_col: str, value_col: str = 'revenue'):
    """In thống kê tổng hợp theo nhóm."""
    stats = df.groupby(group_col)[value_col].agg(['sum', 'mean', 'count'])
    stats.columns = ['Tổng', 'Trung bình', 'Số đơn']
    stats = stats.sort_values('Tổng', ascending=False)
    print(f"\n📊 Thống kê {value_col} theo {group_col}:")
    print(stats.to_string())
    return stats
