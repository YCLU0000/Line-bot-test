# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 21:47:22 2022

@author: David Tsai
"""
import pandas as pd

def multi_flex(df) :
    # select name, link , star, address, opentime, offcial website
    store1 = [df.loc[0,"title"], df.loc[0,"link"],float(df.loc[0,"rating"]),df.loc[0,"address"],df.loc[0,"nextOpenTime"], df.loc[0, "website"]]
    store2 = [df.loc[1,"title"], df.loc[1,"link"],float(df.loc[1,"rating"]),df.loc[1,"address"],df.loc[1,"nextOpenTime"], df.loc[1, "website"]]
    store3 = [df.loc[2,"title"], df.loc[2,"link"],float(df.loc[2,"rating"]),df.loc[2,"address"],df.loc[2,"nextOpenTime"], df.loc[2, "website"]]
    store4 = [df.loc[3,"title"], df.loc[3,"link"],float(df.loc[3,"rating"]),df.loc[3,"address"],df.loc[3,"nextOpenTime"], df.loc[3, "website"]]
    store5 = [df.loc[4,"title"], df.loc[4,"link"],float(df.loc[4,"rating"]),df.loc[4,"address"],df.loc[4,"nextOpenTime"], df.loc[4, "website"]]
    
    # one star
    star1 = ["https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
             "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",
             "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",
             "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",
             "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"]
    # two star
    star2 = ["https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
             "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
             "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",
             "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",
             "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"]
    # three star
    star3 = ["https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
             "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
             "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
             "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",
             "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"]
    # four star
    star4 = ["https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
             "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
             "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
             "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
             "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"]
    # five star
    star5 = ["https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
             "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
             "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
             "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
             "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"]
    star_list = [star1, star2, star3, star4, star5]
    
    # change star list
    store1.append(star_list[round(store1[2])-1])
    store2.append(star_list[round(store2[2])-1])
    store3.append(star_list[round(store3[2])-1])
    store4.append(star_list[round(store4[2])-1])
    store5.append(star_list[round(store5[2])-1])
    
    # append acutual star
    store1[len(store1) - 1].append(store1[2])
    store2[len(store2) - 1].append(store2[2])
    store3[len(store3) - 1].append(store3[2])
    store4[len(store4) - 1].append(store4[2])
    store5[len(store5) - 1].append(store5[2])
    
    # get length of store list
    len1 = len(store1)
    len2 = len(store2)
    len3 = len(store3)
    len4 = len(store4)
    len5 = len(store5)
    
    content = {
  "type": "carousel",
  "contents": [
      {
       # block1
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": store1[5]
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": store1[0],
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "md",
        "contents": [
          {
            "type": "icon",
            "size": "sm",
            "url": store1[len1][0]
          },
          {
            "type": "icon",
            "size": "sm",
            "url": store1[len1][1]
          },
          {
            "type": "icon",
            "size": "sm",
            "url": store1[len1][2]
          },
          {
            "type": "icon",
            "size": "sm",
            "url": store1[len1][3]
          },
          {
            "type": "icon",
            "size": "sm",
            "url": store1[len1][4]
          },
          {
            "type": "text",
            "text": str(store1[len1][5]),
            "size": "sm",
            "color": "#999999",
            "margin": "md",
            "flex": 0
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "Place",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": store1[3],
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "Time",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": store1[4],
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "Google Map",
          "uri": store1[1]
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "官方網站",
          "uri": store[5]
        }
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "margin": "sm"
      }
    ],
    "flex": 0
  }
},
      {
       # Block2
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": store2[5]
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": store2[0],
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "md",
        "contents": [
          {
            "type": "icon",
            "size": "sm",
            "url": store2[len2][0]
          },
          {
            "type": "icon",
            "size": "sm",
            "url": store2[len2][1]
          },
          {
            "type": "icon",
            "size": "sm",
            "url": store2[len2][2]
          },
          {
            "type": "icon",
            "size": "sm",
            "url": store2[len2][3]
          },
          {
            "type": "icon",
            "size": "sm",
            "url": store2[len2][4]
          },
          {
            "type": "text",
            "text": str(store2[len2][5]),
            "size": "sm",
            "color": "#999999",
            "margin": "md",
            "flex": 0
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "Place",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": store2[3],
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "Time",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": store2[4],
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "Google Map",
          "uri": store2[1]
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "官方網站",
          "uri": store2[5]
        }
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "margin": "sm"
      }
    ],
    "flex": 0
  }
},
      {
       # Block3
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": store3[5]
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": store3[0],
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "md",
        "contents": [
          {
            "type": "icon",
            "size": "sm",
            "url": store3[len3][0]
          },
          {
            "type": "icon",
            "size": "sm",
            "url": store3[len3][1]
          },
          {
            "type": "icon",
            "size": "sm",
            "url": store3[len3][2]
          },
          {
            "type": "icon",
            "size": "sm",
            "url": store3[len3][3]
          },
          {
            "type": "icon",
            "size": "sm",
            "url": store3[len3][4]
          },
          {
            "type": "text",
            "text": str(store3[len3][5]),
            "size": "sm",
            "color": "#999999",
            "margin": "md",
            "flex": 0
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "Place",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": store3[3],
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "Time",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": store3[4],
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "Google Map",
          "uri": store3[1]
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "官方網站",
          "uri": store3[5]
        }
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "margin": "sm"
      }
    ],
    "flex": 0
  }
},
      {
       # Block4
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": store4[5]
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": store4[0],
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "md",
        "contents": [
          {
            "type": "icon",
            "size": "sm",
            "url": store4[len4][0]
          },
          {
            "type": "icon",
            "size": "sm",
            "url": store4[len4][1]
          },
          {
            "type": "icon",
            "size": "sm",
            "url": store4[len4][2]
          },
          {
            "type": "icon",
            "size": "sm",
            "url": store4[len4][3]
          },
          {
            "type": "icon",
            "size": "sm",
            "url": store4[len4][4]
          },
          {
            "type": "text",
            "text": str(store4[len4][5]),
            "size": "sm",
            "color": "#999999",
            "margin": "md",
            "flex": 0
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "Place",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": store4[3],
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "Time",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": store4[4],
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "Google Map",
          "uri": store4[1]
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "官方網站",
          "uri": store4[5]
        }
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "margin": "sm"
      }
    ],
    "flex": 0
  }
},
      {
       # Block5
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": store5[5]
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": store5[0],
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "md",
        "contents": [
          {
            "type": "icon",
            "size": "sm",
            "url": store5[len5][0]
          },
          {
            "type": "icon",
            "size": "sm",
            "url": store5[len5][1]
          },
          {
            "type": "icon",
            "size": "sm",
            "url": store5[len5][2]
          },
          {
            "type": "icon",
            "size": "sm",
            "url": store5[len5][3]
          },
          {
            "type": "icon",
            "size": "sm",
            "url": store5[len5][4]
          },
          {
            "type": "text",
            "text": str(store5[len5][5]),
            "size": "sm",
            "color": "#999999",
            "margin": "md",
            "flex": 0
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "Place",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": store5[3],
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "Time",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": store5[4],
                "wrap": True,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "Google Map",
          "uri": store5[1]
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "官方網站",
          "uri": store5[5]
        }
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "margin": "sm"
      }
    ],
    "flex": 0
  }
}
  ]
}
    return(content)
if __name__ == "__main__":
    store = {
    "title": ["Mike", "Sherry", "Cindy", "John","David"],
    "link": [80, 75, 93, 86,99],
    "rating": [1, 2, 2, 3,4.5],
    "address": ["","","","",""],
    "nextOpenTime": ["","","","",""]
}
    df = pd.DataFrame(store)
    flexmessage = multi_flex(df)
