<?php include 'template/header.php'; ?>
  <body>
    
    <section class="ftco-section bg-light">
      <div class="container">
        <div class="row justify-content-center mb-5 pb-5">
          <div class="col-md-7 text-center heading-section ftco-animate">
         
           
          </div>
        </div>
        <div class="row">
          <div class="col-md-12 dish-menu">

            <div class="nav nav-pills justify-content-center ftco-animate" id="v-pills-tab" role="tablist" aria-orientation="vertical">
              <a class="nav-link py-3 px-4 active" id="v-pills-home-tab" data-toggle="pill" href="#v-pills-home" role="tab" aria-controls="v-pills-home" aria-selected="true">Job Seeker Login</a>
              <a class="nav-link py-3 px-4" id="v-pills-profile-tab" data-toggle="pill" href="#v-pills-profile" role="tab" aria-controls="v-pills-profile" aria-selected="false">Organization Login</a>
            </div>

            <!--register as customer-->
            <div class="tab-content py-5" id="v-pills-tabContent">
              <div class="tab-pane fade show active" id="v-pills-home" role="tabpanel" aria-labelledby="v-pills-home-tab">
                <div class="row">
                  <div class="col-lg-2"></div>
                  <div class="col-lg-8">
                    <div class="menus d-flex ftco-animate" style="background: white;">
                      <div class="row" style="width: 100%">
                  <div class="col-md-12">
                    
                      <!-- register as customer -->
                      <form action="manage-insert.php" method="POST" enctype="multipart/form-data">
                       
                        <div class="form-group">
                          <input type="email" name="email" class="form-control" required="" placeholder="Your Email">
                        </div>
                       
                       
                        <div class="form-group">
                          <input type="password" name="password" class="form-control" required="" placeholder="Your Password">
                        </div>
                        
                        <div class="form-group">
                          <input type="submit" value="Login" name="regascus" class="btn btn-primary py-3 px-5">
                        </div>
                      </form>
                      <p class="text-center">Forget password  <a href="login.php">Click Here</a> </p>
                  </div>
              </div>
                  </div>
                  </div>
                </div>
              </div><!-- END -->

              <!--register as organization login-->
              <div class="tab-pane fade" id="v-pills-profile" role="tabpanel" aria-labelledby="v-pills-profile-tab">
                <div class="row">
                  <div class="col-lg-2"></div>
                  <div class="col-lg-8">
                    <div class="menus d-flex ftco-animate" style="background: white;">
                      <div class="row" style="width: 100%">
                  <div class="col-md-12">
                      <form action="manage-insert.php" method="POST" enctype="multipart/form-data">
                        
                        <div class="form-group">
                          <input type="email" name="email" class="form-control" required="" placeholder="Email">
                        </div>
                       
                
                      
                        <div class="form-group">
                          <input type="password" name="password" class="form-control" required="" placeholder="Password">
                        </div>
                      
                        <div class="form-group">
                          <input type="submit" value="Login" name="regasres" class="btn btn-primary py-3 px-5">
                        </div>
                      </form>
                      <p class="text-center">For Login <a href="login.php">Click Here</a> </p>
                  </div>
              </div>
                  </div>
                  </div>
                </div>
              </div><!-- END -->
            </div>
          </div>
        </div>
      </div>
    </section>

   
    
    <?php include 'template/script.php'; ?> 
    
  </body>
</html>