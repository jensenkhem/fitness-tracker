# Database Build/Run Instructions

## Build the Image
From this directory, run the following command:
```
docker build . -t fitness-tracker-db-image
```

## Run the Image
Once the image is built, run the following command to spin it up and expose it on port 5432:
```
docker run -d -p 5432:5432 --name fitness-tracker-db-container fitness-tracker-db-image
```


