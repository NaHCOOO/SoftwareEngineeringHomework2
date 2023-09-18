import re
import jieba
from collections import Counter


def paper_review(original_filename, copied_filename, answer_filename):
    """
    论文查重算法
    :param original_filename: 原论文文件地址
    :param copied_filename: 被查重论文文件地址
    :param answer_filename: 查重结果输出文件地址
    :return:
    """
    try:
        with open(original_filename, 'r', encoding='utf-8') as file:
            original_text = file.read()

        with open(copied_filename, 'r', encoding='utf-8') as file:
            copied_text = file.read()

        original_words = clean_text(original_text)
        copied_words = clean_text(copied_text)

        similarity = calculate_similarity(original_words, copied_words)

        with open(answer_filename, 'w', encoding='utf-8') as file:
            file.write(f"{similarity:.2%}")

        print(f"重复率：{similarity:.2%} (结果已保存至答案文件)")
    except Exception as e:
        print("程序出现错误: ", e)


def clean_text(text):
    """
    文本预处理
    :param text: 文本
    :return: 预处理的结果
    """
    # 去除标点符号和空格
    text = re.sub('[^\w\s]', '', text)
    # 分词并转换为小写
    words = jieba.lcut(text.lower())
    return words


def calculate_similarity(original_words, copied_words):
    """
    计算余弦相似度
    :param original_words: 原文分词
    :param copied_words: 被查文章分词
    :return:
    """

    # 计算词频
    original_freq = Counter(original_words)
    copied_freq = Counter(copied_words)

    # 计算相似度
    return sum((original_freq & copied_freq).values()) / sum((original_freq | copied_freq).values())
