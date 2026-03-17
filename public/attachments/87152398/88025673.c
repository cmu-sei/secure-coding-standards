#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
  char *realpath_res = NULL;

  /* Verify argv[1] is supplied and valid */

  /*
   * Note: 200806 is an estimated date. Please check this when the 2008
   * revision of POSIX is published
   */
#if _POSIX_VERSION >= 200806L || defined (linux)  
  puts("New realpath() implementation available.\n");
  realpath_res = realpath(argv[1], NULL);
#else

  size_t path_size = 0;

#ifdef PATH_MAX /* PATH_MAX is defined */

  path_size = (size_t)PATH_MAX;

#else /* PATH_MAX is not defined */

  long pc_result;

  errno = 0;
  pc_result = pathconf(argv[1], _PC_PATH_MAX); /* Query for PATH_MAX */

  if ( (pc_result == -1) && (errno != 0) ) {
    fprintf(stderr, "pathconf() error.\n");
    /* Handle pathconf() error */
  }
  else if (pc_result == -1) {
    /* Handle unbounded path error */
  }
  else if (pc_result <= 0) {
    /* Handle invalid path error */
  }
  path_size = (size_t)pc_result;

#endif

  char *canonicalized_file = NULL;

  if (path_size > 0) {
    canonicalized_file = malloc(path_size);

    if (canonicalized_file == NULL) {
      /* Handle malloc() error */
    }

    realpath_res = realpath(argv[1], canonicalized_file);
  }

  if (realpath_res == NULL) {
    /* Handle realpath() error */
  }

#endif

  /* Verify file name */

  fopen(realpath_res, "w");

  printf("realpath = %s.\n", realpath_res);

  /* ... */

  
#if _POSIX_VERSION >= 200806L || defined (linux)  
  free(realpath_res);   
  realpath_res = NULL;
#else 
  free(canonicalized_file);
  canonicalized_file = NULL;
#endif

  return 0;

}
