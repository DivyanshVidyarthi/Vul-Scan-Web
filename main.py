from crawler import crawl
from scanner import scan
from report import generate_report

def main():
    target_url = input("Where is the target boss!:").strip()
    
    print(f"\nlet me teach him a lesson boss!... aye {target_url} smart guy!!!\n")

    url = crawl(target_url)

    print(f"Boss it got {len(url)} sub-domains!")

    result = scan(url)

    generate_report(result)

if __name__ == '__main__':
    main()
