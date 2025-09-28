#/bin/bash
root_dir=$(pwd)
output_dir="${root_dir}/_sdk_tmp_"
swagger_json="${root_dir}/swagger.json"

rm -rf $output_dir

export JAVA_OPTS="-Xmx8g" 
openapi-generator-cli generate -i $swagger_json \
    -g python \
    -o $output_dir \
    --library urllib3 \
    --package-name buybtcpay \
    --additional-properties=packageVersion=0.3.0

cp -a $output_dir/. $root_dir/

cp -rf $root_dir/extra/buybtcpay/app $root_dir/buybtcpay
cp -rf $root_dir/extra/test/app $root_dir/test

echo "sonyflake >= 2.0" >> $root_dir/requirements.txt
echo "cryptography >= 45.0" >> $root_dir/requirements.txt

rm -rf $output_dir

echo "Update license and version in pyprpoject.toml"