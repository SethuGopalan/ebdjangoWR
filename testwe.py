{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "b519b9d4-64e7-4049-abcc-367b7d358a13",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import json\n",
    "import pandas as pd\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "10a1644f-b8d6-4b17-a417-28be7d08bfb1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "4b2ae266-cbfe-44b1-b613-4230ec4436ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "1e49c670-a797-4b90-bf2b-dbb9e2e0b71a",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://granite.accuweather.com/hosted/granite/index.asp'\n",
    "r = requests.get(url)\n",
    "json = r.json()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "367811ab-b3c3-47cd-84d5-34c96fb2633c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "3640ca64-03bc-4bbe-9a31-4b2bf1b1aa5c",
   "metadata": {},
   "outputs": [
    {
     "ename": "JSONDecodeError",
     "evalue": "Expecting value: line 1 column 1 (char 0)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mJSONDecodeError\u001b[0m                           Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-19-4c72063d9733>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mjson\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mr\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mjson\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32mc:\\python\\lib\\site-packages\\requests\\models.py\u001b[0m in \u001b[0;36mjson\u001b[1;34m(self, **kwargs)\u001b[0m\n\u001b[0;32m    898\u001b[0m                     \u001b[1;31m# used.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    899\u001b[0m                     \u001b[1;32mpass\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 900\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mcomplexjson\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mloads\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    901\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    902\u001b[0m     \u001b[1;33m@\u001b[0m\u001b[0mproperty\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\python\\lib\\json\\__init__.py\u001b[0m in \u001b[0;36mloads\u001b[1;34m(s, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook, **kw)\u001b[0m\n\u001b[0;32m    355\u001b[0m             \u001b[0mparse_int\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mparse_float\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m \u001b[1;32mand\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    356\u001b[0m             parse_constant is None and object_pairs_hook is None and not kw):\n\u001b[1;32m--> 357\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0m_default_decoder\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdecode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ms\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    358\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mcls\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    359\u001b[0m         \u001b[0mcls\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mJSONDecoder\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\python\\lib\\json\\decoder.py\u001b[0m in \u001b[0;36mdecode\u001b[1;34m(self, s, _w)\u001b[0m\n\u001b[0;32m    335\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    336\u001b[0m         \"\"\"\n\u001b[1;32m--> 337\u001b[1;33m         \u001b[0mobj\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mend\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mraw_decode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ms\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0midx\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0m_w\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ms\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    338\u001b[0m         \u001b[0mend\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_w\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ms\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mend\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    339\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mend\u001b[0m \u001b[1;33m!=\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ms\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\python\\lib\\json\\decoder.py\u001b[0m in \u001b[0;36mraw_decode\u001b[1;34m(self, s, idx)\u001b[0m\n\u001b[0;32m    353\u001b[0m             \u001b[0mobj\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mend\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mscan_once\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ms\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0midx\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    354\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mStopIteration\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0merr\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 355\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mJSONDecodeError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Expecting value\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0ms\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0merr\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvalue\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    356\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mobj\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mend\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mJSONDecodeError\u001b[0m: Expecting value: line 1 column 1 (char 0)"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ae438cc7-0f3d-43ea-9ca4-9afa03d45938",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'json' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-2c11a81f75b5>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mjson\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mkeys\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'json' is not defined"
     ]
    }
   ],
   "source": [
    "json.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c7617152-5ee3-4b78-9a5c-9e36d0fe7497",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5eba91d5-088c-45d1-88c9-23be5917bfc1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6e95d830-6e2f-44c2-bde2-f63021b40b80",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
