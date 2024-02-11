/**
 * Title: RodriguezAlvarado-Projections.js
 * Author: Zadkiel Rodriguez Alvarado
 * Data: 02/11/2024
 * Description: MongoDB Shell
 * Sources:
 *       https://www.mongodb.com/docs/mongodb-shell/write-scripts/
 *       https://learn-us-east-1-prod-fleet01-xythos.content.blackboardcdn.com/blackboard.learn.xythos.prod/5a31d48b683a8/23683846?X-Blackboard-S3-Bucket=blackboard.learn.xythos.prod&X-Blackboard-Expiration=1707696000000&X-Blackboard-Signature=MNe7JyX%2FSpyc%2FLg8XM6zu5P3gXHwO6CszR9xB8t3d4s%3D&X-Blackboard-Client-Id=100225&X-Blackboard-S3-Region=us-east-1&response-cache-control=private%2C%20max-age%3D21600&response-content-disposition=inline%3B%20filename%2A%3DUTF-8%27%27WEB%2520335%2520MongoDB%2520Query%2520Guide.pdf&response-content-type=application%2Fpdf&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLWVhc3QtMSJHMEUCIQCfZz%2BLap650DZ8KoC4Bjo2LKQIhAbPuj%2Bw%2B6ZwpbvgSAIgIJ2RB38Rd%2BfKdNMB0LZuOpbuARPKQF6chOdaLyaE2mYqswUIShAAGgw1NTY5MDM4NjEzNjEiDCqrSWUl22f74oUf3iqQBflEDzjKv23ZOaFe4ehpETw200QbdrxaZVwRCMw6pBnqKXvjijPLIicMz6u36wzFdVTqnVhPDjEfhF39G2L%2F%2BH3%2BX7E5Zso8SlcDPVhMIOv6oWGeweebMV63gl4sx9H7xVTj7KwtcVJQulWs0hliTO%2F5TkrOKrixbo%2F7WqMuVbJlsVXJzssdSwTDCuL3JqwfKh0kwDrBfhnt13EpBQJQfl0aqfGBvjQintqr0b3L9GPmZnFq88T%2B9Z%2Bg7rv72nJO3rqK0zJftQC8SCXEuK6%2FwI6Hlge08pRphCnoMK%2Bs%2FPRAkRKrmXn7RXPPRfwqPHiZFXP5e6oQLoiIqkInaovsZMZPxGq72o06rLuSqxgsajpInNrJKRmeU0f%2BAY6tiRn%2BUjCTvNfeAClV%2FO8eebYCLtCe12sMKqKXNktUQL1VsbpxZ7rHLCNMfTnd%2B%2Frh8ZgDIi5WuTHONzDL9PrV2nE1NFxN2DqTbHERJ9K2svrx373A%2BX7bFsGV36jrOMJuL8mIjBIteN780yDTVh5tGSCctQNG59Fa%2FudokPO8Ko%2BFrFS93uf3wKFMuGPaJORKun3pJMThMIntpYsAzOsioKoK2XB4uNhAL%2F6VH3hn032DWCTFhLat1fFDB%2Fz%2BA2rFMNAjTXAJy8AL89HSkz4fcaMa5OigVXU0pJ4anopWs2PUcoV5q2sYbURIby4cboGSolXP13%2BkTxA6QzXPyPOii%2FMpSwjMZDbtgIb3uhDfr5a8ljmwQc9wDNNmsgGOK4dlC1g8VUTxeFB9JAUdlsvAEiad4J6VgAVtaM6NRWVkltMI3taBRU5Qu2i%2FlYujvsf9tp6KC7TnnFmH3wZPObs4QCNSsGYrjW%2BhSP5zqqp2B2cMgEfEMPCCpK4GOrEBn%2BI332Ool096vkoIKcVu5lS9Wn73A6k05a38Mky7%2F3APq7tyuJQRZI7QGw1u3ocbSvhXGZ1gEWm93%2F8Ikp%2BE4pNyRSIN1%2FohZzfgcsBbnxUxM66ufVhZJqdeohjcxWR7fWfUih05LJiuYxpOUF8kafXXtihkHWXM%2BotTOa8KvzZMu0R60Ux7RXF744FrY1%2FPGh6yCj5Cw38gfGm3A9ypqUPPS5uIStQJe9WdlhdEtJhZ&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240211T180000Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=ASIAYDKQORRYQ6DD5576%2F20240211%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=09dc5de0a4be73adfdf9ea3fe4402ebf85b0bceb39ae0aa61429156be7151d81
 */
// Load users.js file
load("users.js")

// Add a new user to the collection
user = {
    "firstName": "Harry",
    "lastName": "Potter",
    "employeeId": "1013",
    "email": "hpotter@me.com",
    "dateCreated": new Date()
}

db.users.insertOne(user)

// Update user email address
db.users.updateOne({"_id": ObjectId("65c90b1ad08805ae006e6653")}, {$set: {"email": "mozart@me.com"}})

// Find all documents in the user's collection and only show their firstName, lastName and email
db.users.find({}, {"firstName": 1, "lastName": 1, "email": 1})