
for path in day*
do
    cd $path
    for file in *.py
    do
        echo $file
        python $file
    done
    cd ..
done

