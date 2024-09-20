import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Function to get titles from Baidu News
def get_baidu_news(search_term):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://news.baidu.com/ns?word={search_term}&tn=news"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    stories = []
    for item in soup.find_all('div', class_='result'):
        title = item.find('a').text.strip()
        link = item.find('a')['href']
        published = 'Unknown Date'  # Default if not found
        # Check if there's a published date available
        pub_date_tag = item.find('span', class_='c-color-gray2')
        if pub_date_tag:
            published = pub_date_tag.text.strip()
        stories.append({'title': title, 'link': link, 'publisher': 'Baidu News', 'published': published})
    return stories

# Function to convert the 'published' string into a 'Month Year' format
def convert_to_month_year(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %Z')
        return date_obj.strftime('%B %Y')
    except ValueError:
        return 'Unknown Date'

def get_baidu_news(search_term):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://news.baidu.com/ns?word={search_term}&tn=news"
    print(f"Fetching URL: {url}")  # Debug print
    response = requests.get(url, headers=headers)
    print(f"Response Status Code: {response.status_code}")  # Debug print
    soup = BeautifulSoup(response.content, 'html.parser')
    stories = []
    for item in soup.find_all('div', class_='result'):
        title = item.find('a').text.strip()
        link = item.find('a')['href']
        published = 'Unknown Date'  # Default if not found
        pub_date_tag = item.find('span', class_='c-color-gray2')
        if pub_date_tag:
            published = pub_date_tag.text.strip()
        stories.append({'title': title, 'link': link, 'publisher': 'Baidu News', 'published': published})
    print(f"Found {len(stories)} stories for keyword: {search_term}")  # Debug print
    return stories

# Chinese keywords list
keywords_chinese = [
    "ESG供应链管理",
    "ESG物流",
    "绿色物流",
    "供应链碳足迹",
    "供应链社会责任",
    "可持续交付",
    "可持续运输方式",
    "环保包装和配送",
    "物流环境影响",
    "ESG分销",
    "可持续供应链创新",
    "可持续物流策略",
    "基于可再生能源的物流",
    "可持续供应链技术采用",
    "环保物流解决方案开发",
    "循环经济中的供应链执行",
    "基于ESG的物流绩效评估",
    "可持续库存管理策略",
    "碳中和供应链建设",
    "通过环保标签改进分销",
    "社会责任与供应链管理的整合",
    "节能仓库操作",
    "利用环保物流平台",
    "可持续采购管理策略",
    "物流部门的生物多样性提升",
    "可持续交通网络设计",
    "减少环境影响的包装技术",
    "ESG数据管理和报告系统",
    "供应链中的能源优化",
    "可持续物流合作伙伴建设",
    "绿色供应链政策与实施",
    "可持续供应链的教育与意识",
    "利用可回收材料",
    "可持续供应链金融",
    "节能物流系统",
    "物流流程中的温室气体减少",
    "创造社会价值与供应链管理",
    "道德供应链管理",
    "与当地社区合作的物流",
    "生态系统保护的供应链设计",
    "废物管理和减少策略",
    "可再生包装解决方案",
    "供应链中的社交距离策略",
    "物流行业的数字化转型",
    "基于人工智能和大数据的可持续供应链",
    "智能物流与可持续性",
    "提高运输效率",
    "生物燃料运输",
    "供应链风险管理与可持续性",
    "绿色认证和标准合规",
    "可持续供应链基准测试",
    "通过环保技术提高生产力",
    "供应链中的水资源优化",
    "可持续供应链咨询服务",
    "应对气候变化的供应链策略",
    "物流部门的可持续领导力",
    "可持续供应链审计与评估",
    "可重复使用的物流资源",
    "供应链中的包容性与多样性",
    "本地供应链的可持续发展"
]

all_stories_chinese = []  # Initialize an empty list to hold all stories from Baidu News

# Collect stories for each Chinese keyword
for keyword in keywords_chinese:
    stories = get_baidu_news(keyword)
    all_stories_chinese.extend(stories)  # Extend the list with the new stories

# Convert the list of all stories to a DataFrame
df_all_stories_chinese = pd.DataFrame(all_stories_chinese)

# Check if 'published' column exists before applying the conversion
if 'published' in df_all_stories_chinese.columns:
    # Apply the conversion function to the 'published' column
    df_all_stories_chinese['published'] = df_all_stories_chinese['published'].apply(convert_to_month_year)
else:
    print("Warning: 'published' column not found in the data.")

# Save the DataFrame to an Excel file
excel_path_chinese = 'baidu_esg_logistics_news_chinese.xlsx'
df_all_stories_chinese.to_excel(excel_path_chinese, index=False)

print(f"All stories saved to {excel_path_chinese}")