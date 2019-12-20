for i in `seq 1 32`
do
    if [ $(($i % 4)) != 0 ] ; then
        j=`printf %02d $i`
        rm -r ./$j
    fi
done