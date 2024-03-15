# Data Lakehouse com Delta Lake para Dados de Transporte Público

## Como usar

**1 - Instale o Java**

~~~bash
sudo apt install default-jdk
~~~

Para conferir se está instalado, use:

~~~bash
java -version
~~~

**2 - Exporte o JAVA_HOME**

Veja se a seguinte pasta existe:

~~~bash
ls /usr/lib/jvm/
~~~

E pegue o path contendo a sua versão do Java e exporte com o comando:
~~~bash
export JAVA_HOME=/caminho/para/o/java
~~~

**3 - Instale o pyspark**
~~~bash
pip install pyspark
~~~

**4 - Instale o Delta Lake**
~~~bash
pip install delta-spark
pip install deltalake
~~~

**5 - Inicie a sessão Spark no seu script:**

~~~python
from pyspark.sql import *
from delta import *

builder = SparkSession.builder.appName("topicos").config("spark.sql.extensions","io.delta.sql.DeltaSparkSessionExtension").config("spark.sql.catalog.spark_catalog","org.apache.spark.sql.delta.catalog.DeltaCatalog")
spark = configure_spark_with_delta_pip(builder).getOrCreate()

print(spark.version)
~~~

**6 - Atualize os paths para os seus dados**
