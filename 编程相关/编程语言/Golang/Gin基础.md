# Gin基础
- gin安装
    -  `go get github.com/gin-gonic/gin`

    - 一个简单的gin实例

        - ```go
            import (
                "github.com/gin-gonic/gin"
                "net/http"
            )
            
            func main(){
            
                router := gin.Default()
            
                router.GET("/", func(c *gin.Context) {
                    c.String(http.StatusOK, "Hello World")
                })
                router.Run(":8000")
            }
            ```

- RESTFUL路由

    - GET类型的路由

        - ```
            router.GET("/", func(c *gin.Context) {})
            ```

    - POST类型的路由

        - ```go
            router.POST("/", func(c *gin.Context) {})
            ```

        - 