import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ContactListComponent } from './contact-list/contact-list.component';
import { BackgroundComponent } from './background/background.component';
import { ContactComponent } from './contact-list/contact/contact.component';
import { CelularPipe } from './pipes/CelularPipe.pipe';
import { ButtonModule } from 'primeng/button';

@NgModule({
  declarations: [
    AppComponent,
    ContactListComponent,
    BackgroundComponent,
    ContactComponent,
    CelularPipe,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ButtonModule
  ],
  providers: [],
  exports:[
    CelularPipe
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
