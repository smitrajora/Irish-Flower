{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "cordless-penetration",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "from flask import Flask, request, jsonify, render_template\n",
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "interracial-spray",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)\n",
    "model = pickle.load(open('model.pkl', 'rb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "lyric-hostel",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('index.html')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "governing-affairs",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/predict',methods=['POST'])\n",
    "def predict():\n",
    "    '''\n",
    "    For rendering results on HTML GUI\n",
    "    '''\n",
    "    int_features = [int(x) for x in request.form.values()]\n",
    "    final_features = [np.array(int_features)]\n",
    "    prediction = model.predict(final_features)\n",
    "\n",
    "    output = round(prediction[0], 2)\n",
    "\n",
    "    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "empirical-petite",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Restarting with stat\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Smit\\anaconda3\\envs\\tensorflow\\lib\\site-packages\\IPython\\core\\interactiveshell.py:3435: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "induced-mirror",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
