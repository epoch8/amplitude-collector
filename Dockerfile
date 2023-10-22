# Build golang application
FROM golang:1.21.1 AS builder

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN go build -o ./bin/ ./cmd/...

# Path: Dockerfile
# Build final image
FROM debian:bookworm-slim

WORKDIR /app

COPY --from=builder /app/bin/ ./

CMD ["/app/amplitude-collector"]
