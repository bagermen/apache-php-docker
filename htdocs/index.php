<!DOCTYPE html>
<html>
  <head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>LAMP STACK</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.8.2/css/bulma.min.css">
  <script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>
  </head>
  <body>
  <section class="hero is-medium is-primary is-bold">
    <div class="hero-body">
      <div class="container has-text-centered">
        <h1 class="title">
          LAMP STACK
        </h1>
        <h2 class="subtitle">
          Your Local Swarm Development Environment
        </h2>
      </div>
    </div>
  </section>
  <section class="section">
    <div class="container">
      <div class="columns">
        <div class="column">
          <h3 class="title is-3 has-text-centered">Environment</h3>
          <hr>
          <div class="content">
            <ul>
              <li><?= $_SERVER["SERVER_SOFTWARE"]; ?></li>
              <li>PHP <?= phpversion(); ?></li>
              <li>
                <?php
                  $link = mysqli_connect("database", "root", "mW9PjVrNWIP0U7VTkBOvM2BFFr8=", null);

                  /* check connection */
                  if (mysqli_connect_errno()) {
                    printf("MySQL connecttion failed: %s", mysqli_connect_error());
                  } else {
                    /* print server version */
                    printf("MySQL Server %s", mysqli_get_server_info($link));
                  }
                  /* close connection */
                  mysqli_close($link);
                ?>
              </li>
            </ul>
          </div>
        </div>
        <div class="column">
          <h3 class="title is-3 has-text-centered">Quick Links</h3>
          <hr>
          <div class="content">
            <ul>
              <li><a href="phpinfo.php" class="has-text-primary">phpinfo()</a></li>
              <li><a href="memcached.php" class="has-text-primary">Test Memcached Connection</a></li>
              <li><a href="mysql.php" class="has-text-primary">Test DB Connection</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>
  </body>
</html>