# build-24-langchain-vcore

The demo will feature a streamlined ordering system tailored for various food chains. This system will allow users to request customized meals, such as "high protein recipes," with recommendations provided from our database. Users can further customize their choices before sending their orders from the app to the restaurant, including delivery details. A unique feature of our system is its ability to remember user preferences for future orders, using vCore to store that data. With the help of Langchain, this setup can be easily adapted by ISVs with minimal modifications needed for other food chains.

# How to use?

1. **Download the project starter code locally**

    ```bash
    git clone https://github.com/khelanmodi/build-24-langchain-vcore.git
    cd build-24-langchain-vcore
    ```

1. **Initialize and activate a virtualenv using:**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

    >**Note** - In Windows, the `.venv` does not have a `bin` directory. Therefore, you'd use the analogous command shown below:

    ```bash
    source .venv/Scripts/activate
    ```

1. **Install the development dependencies as an editable package:**

    ```bash
    python3 -m pip install -e 'app[dev]'
    ```

1. **Run the [notebook](./CBD_Mongo_vCore.ipynb) to generate the .env file and test out everything**
