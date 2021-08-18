# stop process with the app name
docker ps -q --filter ancestor="PersonPetFood" | xargs -r docker stop
# force delete old images with app name
docker rmi $(docker images 'PersonPetFood' -a -q) --force
# build container
docker build -t PersonPetFood .
# run container
docker run  -dp 5000:5000 PersonPetFood
# run tests
docker exec   $(docker ps | grep 'PersonPetFood' | awk '{ print $1 }') py.test
# run behave
docker exec   $(docker ps | grep 'PersonPetFood' | awk '{ print $1 }') py.test
