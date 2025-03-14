import random

previous_numbers = [20, 21, 22, 25, 28, 29]

hot_numbers = [1, 12, 27, 34, 43]
low_numbers = list(range(1, 23))
high_numbers = list(range(23, 46))

def generate_lotto_numbers():
    odd_numbers = [num for num in range(1, 46) if num % 2 != 0 and num not in previous_numbers]
    even_numbers = [num for num in range(1, 46) if num % 2 == 0 and num not in previous_numbers]
    
    odd_selected = random.sample(odd_numbers, 3)
    even_selected = random.sample(even_numbers, 3)
    
    return sorted(odd_selected + even_selected)

def generate_balanced_numbers():
    low_selected = random.sample([num for num in low_numbers if num not in previous_numbers], 3)
    high_selected = random.sample([num for num in high_numbers if num not in previous_numbers], 3)
    
    return sorted(low_selected + high_selected)

def generate_lotto_with_hot_numbers():
    selected_numbers = set(random.sample([num for num in hot_numbers if num not in previous_numbers], 2))
    remaining_numbers = set(range(1, 46)) - selected_numbers - set(previous_numbers)
    remaining_selected = random.sample(list(remaining_numbers), 4)
    
    return sorted(list(selected_numbers) + remaining_selected)

def generate_combined_lotto():
    used_numbers = set()
    hot_selected = set(random.sample([num for num in hot_numbers if num not in previous_numbers], 2))
    used_numbers.update(hot_selected)
  
    low_selected = random.sample([num for num in low_numbers if num not in used_numbers and num not in previous_numbers], 2)
    high_selected = random.sample([num for num in high_numbers if num not in used_numbers and num not in previous_numbers], 2)
  
    odd_numbers = [num for num in range(1, 46) if num % 2 != 0 and num not in used_numbers and num not in previous_numbers]
    even_numbers = [num for num in range(1, 46) if num % 2 == 0 and num not in used_numbers and num not in previous_numbers]
  
    odd_selected = random.sample(odd_numbers, 2)
    even_selected = random.sample(even_numbers, 2)
  
    all_selected = list(hot_selected) + low_selected + high_selected + odd_selected + even_selected
    
    return sorted(random.sample(all_selected, 6))

def generate_lotto():
    print("핫 넘버 포함 로또 번호:", generate_lotto_with_hot_numbers())
    print("홀수/짝수 비율 맞춘 번호:", generate_lotto_numbers())
    print("고/저 숫자 균형 맞춘 번호:", generate_balanced_numbers())
    print("세 가지 전략을 조합한 로또 번호:", generate_combined_lotto())

generate_lotto()
