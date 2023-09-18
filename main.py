import sys

from utils.paper_review_utils import calculate_similarity, paper_review


def main():
    if len(sys.argv) != 4:
        print("请提供正确的文件路径参数")
        return

    original_filename = sys.argv[1]
    copied_filename = sys.argv[2]
    answer_filename = sys.argv[3]
    paper_review(original_filename, copied_filename, answer_filename)


if __name__ == "__main__":
    main()
