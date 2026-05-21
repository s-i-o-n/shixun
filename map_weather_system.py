"""
高德地图 + 天气 + IP 查询综合小系统
==========================================

功能菜单：
1. 查询地址经纬度（地理编码）
2. 查询经纬度对应地址（逆地理编码）
3. 查询当前 IP 地址
4. 查询城市天气
5. 周边搜索
0. 退出
"""

import requests
import json
from datetime import datetime

# ============================================================================
# 配置区 - 请替换为你的真实 API Key
# ============================================================================

AMAP_KEY = "fe3b492b1dc28ed2f600acdc963c83aa"  # 高德 API Key
WEATHER_KEY = "你的和风天气Key"                # 和风天气 API Key（可选）


# ============================================================================
# 工具函数
# ============================================================================

def print_divider(char="=", length=50):
    """打印分隔线，美化输出"""
    print(char * length)


def print_section(title):
    """打印带格式的章节标题"""
    print()
    print_divider()
    print(f"  {title}")
    print_divider()


# ============================================================================
# 功能 1：地理编码 - 地址 → 坐标
# ============================================================================

def geo_address():
    """
    根据地址查询经纬度坐标
    
    使用高德地理编码 API：
    https://restapi.amap.com/v3/geocode/geo
    """
    print_section("地理编码（地址 → 坐标）")
    
    address = input("请输入要查询的地址（如：新余学院）：").strip()
    if not address:
        print("地址不能为空！")
        return
    
    city = input("请输入城市名（可选，直接回车跳过）：").strip()
    
    # 构建请求参数
    params = {
        "key": AMAP_KEY,
        "address": address,
    }
    if city:
        params["city"] = city
    
    # 发送请求
    url = "https://restapi.amap.com/v3/geocode/geo"
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()          # 如果 HTTP 状态码不是 200，抛出异常
        result = response.json()
    except requests.exceptions.Timeout:
        print("请求超时，请检查网络连接！")
        return
    except requests.exceptions.RequestException as e:
        print(f"网络请求失败：{e}")
        return
    
    # 解析结果
    if result.get("status") == "1" and result.get("geocodes"):
        geo = result["geocodes"][0]          # 取第一个结果（最相关）
        lng, lat = geo["location"].split(",")  # 拆分经纬度
        
        # 格式化输出
        print()
        print(f"  查询地址：{address}")
        print(f"  标准地址：{geo.get('formatted_address', '未知')}")
        print(f"  经度 lng：{lng}")
        print(f"  纬度 lat：{lat}")
        print(f"  行政区划：{geo.get('province', '')} {geo.get('city', '')} {geo.get('district', '')}")
        print(f"  匹配级别：{geo.get('level', '未知')}")  # 省/市/区县/道路...
    else:
        print(f"查询失败：{result.get('info', '未知错误')}")


# ============================================================================
# 功能 2：逆地理编码 - 坐标 → 地址
# ============================================================================

def reverse_geo():
    """
    根据经纬度坐标查询对应地址
    
    使用高德逆地理编码 API：
    https://restapi.amap.com/v3/geocode/regeo
    """
    print_section("逆地理编码（坐标 → 地址）")
    
    try:
        lng = input("请输入经度（如 114.9171）：").strip()
        lat = input("请输入纬度（如 27.8179）：").strip()
        if not lng or not lat:
            print("经度和纬度不能为空！")
            return
        # 尝试转换成浮点数，顺便检查格式是否正确
        float(lng)
        float(lat)
    except ValueError:
        print("坐标格式不正确，请输入数字！")
        return
    
    params = {
        "key": AMAP_KEY,
        "location": f"{lng},{lat}",
        "extensions": "all",
    }
    
    url = "https://restapi.amap.com/v3/geocode/regeo"
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        result = response.json()
    except requests.exceptions.RequestException as e:
        print(f"网络请求失败：{e}")
        return
    
    if result.get("status") == "1":
        regeo = result["regeocode"]
        addr = regeo["addressComponent"]
        
        print()
        print(f"  输入坐标：{lng}, {lat}")
        print(f"  完整地址：{regeo.get('formatted_address', '未知')}")
        print(f"  省份：{addr.get('province', '未知')}")
        print(f"  城市：{addr.get('city', '未知')}")
        print(f"  区县：{addr.get('district', '未知')}")
        print(f"  街道：{addr.get('township', '未知')}")
        
        # 如果有详细的街道地址信息
        street_info = regeo.get("streetAddress", {})
        if street_info:
            print(f"  路名：{street_info.get('street', '未知')} {street_info.get('number', '')}号")
    else:
        print(f"查询失败：{result.get('info', '未知错误')}")


# ============================================================================
# 功能 3：查询当前 IP 地址
# ============================================================================

def get_ip_address():
    """
    查询本机公网 IP 地址
    
    使用 httpbin.org/ip 这个免费接口
    返回格式：{"origin": "xxx.xxx.xxx.xxx"}
    """
    print_section("查询当前 IP 地址")
    
    try:
        print("正在查询，请稍候...")
        response = requests.get("https://httpbin.org/ip", timeout=10)
        response.raise_for_status()
        
        # httpbin 返回的是纯 JSON 字符串，用 json.loads 解析
        data = response.json()
        ip = data.get("origin", "未知")
        
        print()
        print(f"  您的公网 IP 地址是：{ip}")
        print(f"  查询时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
    except requests.exceptions.Timeout:
        print("请求超时，请检查网络连接！")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP 错误：{e}")
    except json.JSONDecodeError as e:
        print(f"解析服务器返回数据失败：{e}")
    except requests.exceptions.RequestException as e:
        print(f"网络请求失败：{e}")


# ============================================================================
# 功能 4：查询城市天气（使用免费天气 API）
# ============================================================================

def get_weather():
    """
    查询城市天气
    
    使用 wttr.in 免费天气 API（无需注册 Key）
    返回格式：纯文本，直接在终端显示
    """
    print_section("查询城市天气")
    
    city = input("请输入城市名称（中文或拼音，如：新余 或 xinyu）：").strip()
    if not city:
        print("城市名称不能为空！")
        return
    
    # wttr.in 是一个免费的天气 API，不需要 Key
    # 支持中文城市名，返回格式化的天气信息
    url = f"https://wttr.in/{city}?format=j1"  # format=j1 返回 JSON
    
    try:
        print("正在查询天气，请稍候...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # 提取当前天气
        current = data["current_condition"][0]
        area = data["nearest_area"][0]
        
        # 城市名称（wttr.in 返回的是英文，这里用输入的城市名）
        city_name = city
        temp_c = current["temp_C"]           # 当前温度（摄氏度）
        feel_like = current["FeelsLikeC"]    # 体感温度
        humidity = current["humidity"]        # 湿度
        wind_speed = current["windspeedKmph"]  # 风速
        weather_desc = current["weatherDesc"][0]["value"]  # 天气描述
        
        print()
        print(f"  城市：{city_name}")
        print(f"  天气：{weather_desc}")
        print(f"  当前温度：{temp_c} °C")
        print(f"  体感温度：{feel_like} °C")
        print(f"  湿度：{humidity} %")
        print(f"  风速：{wind_speed} km/h")
        print(f"  查询时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
    except requests.exceptions.RequestException as e:
        print(f"查询失败：{e}")
        print("提示：可以尝试输入城市的拼音，如 beijing、shanghai")
    except (KeyError, json.JSONDecodeError):
        print("解析天气数据失败，请检查城市名称是否正确！")


# ============================================================================
# 功能 5：周边搜索
# ============================================================================

def nearby_search():
    """
    搜索指定地址周边的地点（餐厅、酒店、景点等）
    
    使用高德周边搜索 API：
    https://restapi.amap.com/v3/place/around
    """
    print_section("周边搜索")
    
    address = input("请输入中心地址（如：新余学院）：").strip()
    if not address:
        print("地址不能为空！")
        return
    
    keywords = input("请输入搜索关键词（如：餐厅、酒店、地铁站）：").strip()
    if not keywords:
        print("关键词不能为空！")
        return
    
    # 第1步：先通过地理编码获取中心坐标
    print("正在获取地址坐标...")
    geo_params = {"key": AMAP_KEY, "address": address}
    try:
        geo_response = requests.get(
            "https://restapi.amap.com/v3/geocode/geo",
            params=geo_params,
            timeout=10
        )
        geo_response.raise_for_status()
        geo_result = geo_response.json()
    except requests.exceptions.RequestException as e:
        print(f"获取坐标失败：{e}")
        return
    
    if geo_result.get("status") != "1" or not geo_result.get("geocodes"):
        print(f"地址解析失败：{geo_result.get('info', '未知错误')}")
        return
    
    lng, lat = geo_result["geocodes"][0]["location"].split(",")
    print(f"中心坐标：经度 {lng}，纬度 {lat}")
    
    # 第2步：用坐标进行周边搜索
    search_params = {
        "key": AMAP_KEY,
        "location": f"{lng},{lat}",
        "keywords": keywords,
        "radius": "2000",   # 搜索半径 2000 米
        "offset": "10",      # 返回 10 条结果
        "page": "1",
        "extensions": "base",
    }
    
    try:
        print("正在搜索周边...")
        response = requests.get(
            "https://restapi.amap.com/v3/place/around",
            params=search_params,
            timeout=10
        )
        response.raise_for_status()
        result = response.json()
    except requests.exceptions.RequestException as e:
        print(f"搜索失败：{e}")
        return
    
    # 第3步：格式化输出结果
    if result.get("status") == "1" and result.get("pois"):
        pois = result["pois"]
        print()
        print(f"在 [{address}] 周边 2000 米内找到 {len(pois)} 个「{keywords}」：")
        print()
        for i, poi in enumerate(pois[:10], 1):  # 最多显示 10 条
            name = poi.get("name", "未知")
            addr = poi.get("address", "地址未知")
            distance = poi.get("distance", "?")
            print(f"  {i}. {name}")
            print(f"     地址：{addr}")
            print(f"     距离：{distance} 米")
            print()
    else:
        print(f"未找到相关结果：{result.get('info', '未知错误')}")


# ============================================================================
# 主菜单
# ============================================================================

def show_menu():
    """显示主菜单"""
    print()
    print("=" * 50)
    print("      高德地图 + 天气 + IP 查询系统")
    print("=" * 50)
    print("  1. 地址 → 经纬度（地理编码）")
    print("  2. 经纬度 → 地址（逆地理编码）")
    print("  3. 查询当前 IP 地址")
    print("  4. 查询城市天气")
    print("  5. 周边搜索")
    print("  0. 退出系统")
    print("=" * 50)


def main():
    """主函数：显示菜单，根据用户选择调用对应功能"""
    print("欢迎使用地图查询系统！")
    print(f"系统启动时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    while True:
        show_menu()
        choice = input("请输入选项（0-5）：").strip()
        
        if choice == "1":
            geo_address()
        elif choice == "2":
            reverse_geo()
        elif choice == "3":
            get_ip_address()
        elif choice == "4":
            get_weather()
        elif choice == "5":
            nearby_search()
        elif choice == "0":
            print()
            print("感谢使用，再见！")
            break
        else:
            print("输入无效，请输入 0-5 之间的数字！")
        
        # 每次功能执行完后，等待用户按回车继续
        input("\n按回车键返回主菜单...")


# ============================================================================
# 程序入口
# ============================================================================

if __name__ == "__main__":
    main()
