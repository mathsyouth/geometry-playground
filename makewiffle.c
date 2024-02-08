#include "stdio.h"
#include "stdlib.h"
#include "math.h"
#include "paulslib.h"
#include "bitmaplib.h"

#define N 200  // Define a constant N which will be the size of the grid

double ***grid;  // Declare a pointer to a 3D array (grid) of doubles

int main(int argc,char **argv)  // Main function with command-line arguments
{
   int i,j,k;  // Declare loop counters
   short int si;  // Declare a short integer for storing the scaled grid values
   double v,vmin=1e32,vmax=-1e32;  // Declare variables for the grid value and its min/max for normalization
   double a,b,da,db;  // Declare variables for coefficients and intermediate calculations
   XYZ p;  // Declare a variable of type XYZ, presumably a struct for 3D points
   BITMAP4 *image,c;  // Declare a pointer to a BITMAP structure and a BITMAP variable for image operations
   COLOUR colour;  // Declare a variable of type COLOUR, presumably a struct for color representation
   char fname[32];  // Declare a character array for filename storage
   FILE *fptr,*fvol;  // Declare file pointers for file operations

   // Allocate memory for the 3D grid
   grid = malloc((N+1)*sizeof(double **));
   for (i=0;i<=N;i++) {
      grid[i] = malloc((N+1)*sizeof(double *));
   }
   for (i=0;i<=N;i++) {
      for (j=0;j<=N;j++) {
         grid[i][j] = malloc((N+1)*sizeof(double));
      }
   }
   // Initialize the grid values to 0
   for (i=0;i<=N;i++) 
      for (j=0;j<=N;j++) 
         for (k=0;k<=N;k++) 
            grid[i][j][k] = 0;

   // Set coefficients a and b for the function to be evaluated on the grid
   a = 1 / 2.3;
   b = 1 / 2.0;

   // Calculate the function values at each point in the grid
   for (i=0;i<=N;i++) {
      fprintf(stderr,"%d ",i);  // Print the current index to the standard error stream
      for (j=0;j<=N;j++) {
         for (k=0;k<=N;k++) {
            // Convert grid indices to spatial coordinates
            p.x = 5 * (i - N/2.0) / (float)N;
            p.y = 5 * (j - N/2.0) / (float)N;
            p.z = 5 * (k - N/2.0) / (float)N;
            // Calculate the function's value at point p
            da = pow(a*p.x,2.0) + pow(a*p.y,2.0) + pow(a*p.z,2.0);
            db = pow(b*p.x,8.0) + pow(b*p.y,8.0) + pow(b*p.z,8.0);
            // Avoid division by zero
            if (da < 0.0001)
               da = 0.0001;
            // Calculate the function's value
            v = 1 - 1.0/(da*da*da*da*da*da) - db*db*db*db*db*db; 
            // Clamp the value to a range to avoid extreme values
            if (v < -20)
               v = -20;
            if (v > 20)
               v = 20;
            // Store the value in the grid and update min/max values
            grid[i][j][k] = v;
            vmin = MIN(vmin,v);  // MIN is presumably a macro or function for finding the minimum
            vmax = MAX(vmax,v);  // MAX is presumably a macro or function for finding the maximum
         }
      }
   }
   // Print the range of the function values to the standard error stream
   fprintf(stderr,"\nRange  = %g -> %g\n",vmin,vmax);

   // Write the grid values to a volume file
   fvol = fopen("wiffle.vol","w");  // Open the file for writing
   // Write some header information to the volume file
   fprintf(fvol,"Wiffle cube\n");
   fprintf(fvol,"%d %d %d\n",N,N,N);
   fprintf(fvol,"1.0 1.0 1.0\n");
   fprintf(fvol,"0.0 0.0 0.0\n");
   fprintf(fvol,"16 1\n");
   // Write the normalized grid values to the file
   for (k=0;k<N;k++) {
      for (j=0;j<N;j++) {
         for (i=0;i<N;i++) {
            // Normalize the value to a short int range
            si = (short int)(10000*(grid[i][j][k]-vmin)/(vmax-vmin));
            // Write the short int to the file
            fwrite(&si,sizeof(short int),1,fvol);
         }
      }
   }
   fclose(fvol);  // Close the volume file

   // Create bitmap images for visualization
   image = Create_Bitmap(N+1,N+1);  // Create a new bitmap image
   // Generate images at various slices of the grid
   for (k=0;k<=N/2;k+=10) {
      for (i=0;i<=N;i++) {
         for (j=0;j<=N;j++) {
            // Get the color corresponding to the grid value
            colour = GetColour(grid[i][j][k],vmin,vmax,1);
            // Convert the color to RGB values
            c.r = colour.r * 255;
            c.g = colour.g * 255; 
            c.b = colour.b * 255; 
            // Draw the pixel on the bitmap
            Draw_Pixel(image,N+1,N+1,i,j,c);
         }
      }
      // Create a filename based on the slice index
      sprintf(fname,"%03d.tga",k);
      fptr = fopen(fname,"w");  // Open the file for writing
      // Write the bitmap to the file
      Write_Bitmap(fptr,image,N+1,N+1,12);
      fclose(fptr);  // Close the file
   }
}