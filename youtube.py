# import pandas as pd
# import json
# import sys
# import time
# import requests

# pd.set_option('display.max_rows', 500)
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.width', 1000)

# YOUTUBE_COMMENTS_AJAX_URL = 'https://www.youtube.com/comment_service_ajax'

# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'

# SORT_BY_POPULAR = 0
# SORT_BY_RECENT = 1

# FILE_NAME = 'ytb_comments.csv'


# def find_value(html, key, num_chars=2, separator='"'):
#     pos_begin = html.find(key) + len(key) + num_chars
#     pos_end = html.find(separator, pos_begin)
#     return html[pos_begin: pos_end]


# def ajax_request(session, url, params=None, data=None, headers=None, retries=5, sleep=20):
#     for _ in range(retries):
#         response = session.post(url, params=params, data=data, headers=headers)
#         if response.status_code == 200:
#             return response.json()
#         if response.status_code in [403, 413]:
#             return {}
#         else:
#             time.sleep(sleep)


# def download_comments(youtube_video_url, sort_by=SORT_BY_RECENT, sleep=.1):
#     session = requests.Session()
#     session.headers['User-Agent'] = USER_AGENT

#     response = session.get(youtube_video_url)
#     html = response.text
#     session_token = find_value(html, 'XSRF_TOKEN', 3)
#     session_token = session_token.encode('ascii').decode('unicode-escape')

#     data = json.loads(find_value(html, 'var ytInitialData = ', 0, '};') + '}')
#     for renderer in search_dict(data, 'itemSectionRenderer'):
#         ncd = next(search_dict(renderer, 'nextContinuationData'), None)
#         if ncd:
#             break

#     if not ncd:
#         # Comments disabled?
#         return

#     needs_sorting = sort_by != SORT_BY_POPULAR
#     continuations = [(ncd['continuation'], ncd['clickTrackingParams'], 'action_get_comments')]
#     while continuations:
#         continuation, itct, action = continuations.pop()
#         response = ajax_request(session, YOUTUBE_COMMENTS_AJAX_URL,
#                                 params={action: 1,
#                                         'pbj': 1,
#                                         'ctoken': continuation,
#                                         'continuation': continuation,
#                                         'itct': itct},
#                                 data={'session_token': session_token},
#                                 headers={'X-YouTube-Client-Name': '1',
#                                          'X-YouTube-Client-Version': '2.20201202.06.01'})

#         if not response:
#             break
#         if list(search_dict(response, 'externalErrorMessage')):
#             raise RuntimeError('Error returned from server: ' + next(search_dict(response, 'externalErrorMessage')))

#         if needs_sorting:
#             sort_menu = next(search_dict(response, 'sortFilterSubMenuRenderer'), {}).get('subMenuItems', [])
#             if sort_by < len(sort_menu):
#                 ncd = sort_menu[sort_by]['continuation']['reloadContinuationData']
#                 continuations = [(ncd['continuation'], ncd['clickTrackingParams'], 'action_get_comments')]
#                 needs_sorting = False
#                 continue
#             raise RuntimeError('Failed to set sorting')

#         if action == 'action_get_comments':
#             section = next(search_dict(response, 'itemSectionContinuation'), {})
#             for continuation in section.get('continuations', []):
#                 ncd = continuation['nextContinuationData']
#                 continuations.append((ncd['continuation'], ncd['clickTrackingParams'], 'action_get_comments'))
#             for item in section.get('contents', []):
#                 continuations.extend([(ncd['continuation'], ncd['clickTrackingParams'], 'action_get_comment_replies')
#                                       for ncd in search_dict(item, 'nextContinuationData')])

#         elif action == 'action_get_comment_replies':
#             continuations.extend([(ncd['continuation'], ncd['clickTrackingParams'], 'action_get_comment_replies')
#                                   for ncd in search_dict(response, 'nextContinuationData')])

#         for comment in search_dict(response, 'commentRenderer'):
#             yield {'cid': comment['commentId'],
#                    'text': ''.join([c['text'] for c in comment['contentText']['runs']]),
#                    'time': comment['publishedTimeText']['runs'][0]['text'],
#                    'author': comment.get('authorText', {}).get('simpleText', ''),
#                    'channel': comment['authorEndpoint']['browseEndpoint']['browseId'],
#                    'votes': comment.get('voteCount', {}).get('simpleText', '0'),
#                    'photo': comment['authorThumbnail']['thumbnails'][-1]['url'],
#                    'heart': next(search_dict(comment, 'isHearted'), False)}

#         time.sleep(sleep)


# def search_dict(partial, search_key):
#     stack = [partial]
#     while stack:
#         current_item = stack.pop()
#         if isinstance(current_item, dict):
#             for key, value in current_item.items():
#                 if key == search_key:
#                     yield value
#                 else:
#                     stack.append(value)
#         elif isinstance(current_item, list):
#             for value in current_item:
#                 stack.append(value)


# def main(url):
#     df_comment = pd.DataFrame()
#     try:
#         youtube_url = url
#         limit = 100
#         comment_df = pd.DataFrame()

#         print('Downloading Youtube comments for video:', youtube_url)

#         count = 0

#         start_time = time.time()

#         for comment in download_comments(youtube_url):

#             df_comment = df_comment.append(comment, ignore_index=True)

#             # comments overview
#             comment_json = json.dumps(comment, ensure_ascii=False)
#             print(comment_json)

#             count += 1

#             if limit and count >= limit:
#                 break

#         print(df_comment.shape, df_comment)

#         # dump to a csv file
#         df_comment.to_csv(FILE_NAME, encoding='utf-8')
#         print('\n[{:.2f} seconds] Done!'.format(time.time() - start_time))

#     except Exception as e:
#         print('Error:', str(e))
#         sys.exit(1)


# youtube_URL = 'https://www.youtube.com/watch?v=Ucbrmw2qtXs'

# main(youtube_URL)



# result = 1
# result=1
# for i in range(1,8):
#     result = result*i
#     if(i%2==0):
#         print(" / ",end="")    
#     else:    
#         print(f"({i}*{i+1})" ,end="")        
# print(" = ",result,end="")

    # (1*2) / (3*4) / (5*6) / (7*8) = 
    
    
    
    
# (1^2) / (2^3) / (3^4) / (4^5) = output
    
    
# result = 1  

# for i in range(2, 7, 2):
#     result *= i / (i - 1)

# print(result)

# result = 1 

# for i in range(2,10):
#     if(i%2==0):
#         result=result*i
#     else:
#         result=result/i
#     print(result)

# (1^2) / (2^3) / (3^4) / (4^5) = output


# (1*2) / (3*4) / (5*6) / (7*8) =  5040 output
# result = 1
# for i in range(2,8):
#     result = result*i
#     if (i*1==0):
#         print(" ",end="")
#     else:
#         print(f"({i}^{i+1})",end=" ")
# print(" = ",result,end="")

        
 
#  odd and even number
   
# num=int(input("enter the number even/odd"))
# for i in range(2,10):
#     if num%2==0:
#         print(num,"is a even number")
#     else:
#         print(num,"is a odd number")


# square

# num = int(input("enter the number of square"))
# print("square",num*num)


# cube

# num=int(input("enter the number of cube"))
# print("cube",num*num*num)



# vowel

# alpha=input("enter the charactor for check vowel and constant")
# if(alpha == 'a' or alpha == 'e' or alpha == 'i' or alpha == 'o' or alpha == 'u'):
#     print(alpha,"is a vowel")
# else:
#     print(alpha,"is a constant")
    
    
    
    
    


# space in string value
# string= input("enter the string :")
# result= ""
# for i in string:
#     if i!="":
#         result+=i
# print("string space :",result)


# n=int(input("Enter the number of terms:"))
# x=int(input("Enter the value of x:"))
# sum1=1
# for i in range(2,n+1):
#     sum1=sum1+((x**i)/i)
# print("The sum of series is",round(sum1,2))


#1.remove palindromes from the given list
# item_list = ["lol", "gone","car", "Nenonen", "stop", "madam",None]
# n_list = []
# for i in item_list:
#      if i and i != i[::-1]:
#          n_list.append(i)

# print(n_list)




# # 2.Write a Python function to find the second largest number in the given list
# item_list = [1,3,2,15,2,1,10,11,69,23,100,2,44,9]
# item_list.sort()
# print("second largest ",item_list[-2])




# # 3.Sort the given array without using any built in python functions
# item_list = [3,1,5,6,2,4]
# for i in range(len(item_list)):
#      for j in range(len(item_list)):
#          if item_list[i-1] > item_list[i]:
#              item_list[i] = item_list[i-1]




# #4. Get the event name and the year from the given text remove the unwanted parts using regex
# import re
# given_text = "Liverpool vs Real Marid Live 2018 Streams"
# expected = re.search('(.*?) Live (.*?)\s+',given_text).group(1) + " "+re.search('(.*?) Live (.*?)\s+',given_text).group(2)
# print(expected)
# #expected output - Liverpool vs Real Madrid 2018




# # 5.Extract the domain names from the given list using regex ['https://www.example.com', 'http://www.test.org']

# dm = ['https://www.example.com', 'http://www.test.org']
# d_name = []
# for i in dm:
#     d_name.append(re.search('w\.(\w+\.\w+)',i).group(1))
# print(d_name)




# # 6.multiply the elements in the list by 2 and remove the odd number from it use Lambda function 
# numbers = [2,3,8.5,5.5]
# print([i*2 for i in list(filter(lambda x:x%2==0,numbers))])



# 7. generate the given pattern using recusive function
# *
# **
# ***
# ****
# *****

# def patrn(n):
#     for i in range(0,n):
#         for j in range(0, i+1):
#             print("*",end="")
#         print("\n")
# n=5
# patrn(n)


def prtn(n):
    if n==0:
        return
    else:
        prtn(n-1)
        print("* "*n)
  
n = 5
prtn(n)


# n=5
# i=1
# j=0
# while(i<=n):
#     while(j<=i-1):
#         print("* ",end="")
#         j+=1
#     print("\n")
#     j=0;i+=1

# n=5
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print("\n")

# a=0
# b=1
# for i in range(2,10):
#     c=a+b
#     print(c)
#     a,b=b,c


# import os
# os.remove("watches.csv")
# print("File Removed!")

# a**0.5

# x=int(input("enter the value" ))
# y=int(input("enter the value"))
# sum=0
# for i in range(x,y):
#     sum=sum+(i/i**0.5)
# print (sum)    



