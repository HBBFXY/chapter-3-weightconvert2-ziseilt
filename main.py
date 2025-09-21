# 在这个文件里编写代码
def main():
    # 起始体重
    current_weight = 50.0
    
    # 每年增长量
    yearly_gain = 0.5
    
    # 月球重力比例
    moon_ratio = 0.165
    
    print("起始体重: 50.0kg")
    print("\n未来10年体重变化预测")
    print("年份\t地球体重(kg)\t月球体重(kg)")
    print("-" * 40)
    
    # 计算并输出未来10年的体重变化
    for year in range(0, 11):
        earth_weight = current_weight + yearly_gain * year
        moon_weight = earth_weight * moon_ratio
        
        print(f"{year}\t{earth_weight:.2f}\t\t{moon_weight:.2f}")

if __name__ == "__main__":
    main()
